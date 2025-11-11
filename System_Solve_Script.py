import numpy as np
import pandas as pd 
#funcs that solve for theoretical defl 
def solve_system(Global_K, Load_External_list, active_DOF,Tot_DOF):

    K_reduced = Global_K[np.ix_(active_DOF, active_DOF)]
    F_reduced = Load_External_list[active_DOF]
    displacements = np.linalg.solve(K_reduced, F_reduced)
    Tot_DOF = Global_K.shape[0]
    full_displacements = np.zeros(Tot_DOF)
    full_displacements[active_DOF] = displacements
    return full_displacements

def pick_T_mat (N_DOF_G_PER_ELEMENT,theta):
    if N_DOF_G_PER_ELEMENT == 4:
        T = np.array([[np.cos(theta), np.sin(theta), 0, 0],
                      [-np.sin(theta), np.cos(theta), 0, 0],
                      [0, 0, np.cos(theta), np.sin(theta)],
                      [0, 0, -np.sin(theta), np.cos(theta)]])
    elif N_DOF_G_PER_ELEMENT == 2:
        T = np.array([[np.cos(theta), np.sin(theta)],
                      [-np.sin(theta), np.cos(theta)]])
    elif N_DOF_G_PER_ELEMENT == 6:
        T = np.array([[np.cos(theta), np.sin(theta), 0, 0, 0, 0],
                      [-np.sin(theta), np.cos(theta), 0, 0, 0, 0],
                      [0, 0, 1, 0, 0, 0],
                      [0, 0, 0, np.cos(theta), np.sin(theta), 0],
                      [0, 0, 0, -np.sin(theta), np.cos(theta), 0],
                      [0, 0, 0, 0, 0, 1]])
    return T

def local_stiff_list(el_type_list,N_DOF_G_PER_ELEMENT):
    Spring_count=0
    Truss_count=0  
    beam_count=0
    Local_stiffness_mat_list = [None] * len(el_type_list)
    for i, el_type in enumerate(el_type_list):

        if el_type == 'spring':
            Local_stiffness_mat_list[i] = spring_stiffness_matrix(k_list[Spring_count],N_DOF_G_PER_ELEMENT) 
            Spring_count+=1

        elif el_type=='truss':
            Local_stiffness_mat_list[i] =truss_stiffness_matrix(L_list[Truss_count], E_list[Truss_count], A_list[Truss_count],N_DOF_G_PER_ELEMENT)
            Truss_count+=1
        elif el_type=='beam':
            Local_stiffness_mat_list[i] =beam_stiffness_matrix(L_list[beam_count], E_list[beam_count],I_list[beam_count], A_list[beam_count],N_DOF_G_PER_ELEMENT)
            beam_count+=1
    return Local_stiffness_mat_list

def Global_stiff_piece_generator(Local_stiffness_mat,theta,N_DOF_G_PER_ELEMENT):
    # Transform the local stiffness matrix to global coordinates
    T = pick_T_mat(N_DOF_G_PER_ELEMENT, theta)  # Transformation matrix
    K_global_piece = T.T @ Local_stiffness_mat @ T  # Transform the local stiffness matrix
    return K_global_piece

def Make_Global_piece_list(el_type_list,Local_stiffness_mat_list,theta_list,N_DOF_G_PER_ELEMENT):
    k_global_piece_list=[None] * len(el_type_list)
    for i in range(len(el_type_list)):
        k_global_piece_list[i] = Global_stiff_piece_generator(Local_stiffness_mat_list[i], theta_list[i],N_DOF_G_PER_ELEMENT)
    return k_global_piece_list

def assemble_global_stiffness_matrix(k_global_piece_list, Global_K,N_DOF_per_node):#might need to change N_DOF_element to a list of DOF per element
    #general steps: 
    #0. Get current element number
    #1. Get Global stiffness piece from k_global_piece_list using el number
    #2. Get associated nodes using con mat
    #3. Get associated DOF by math [0,1,2]+(current node num*ndof per node)or[0,1,2,3,4,5]+(current el num*ndof per node)
    #4. Insert global pieces into assembly...
    #    ix func: can use array of indicies to insert shit 
   
    #i corresponds to element numbering

    #current dof indices might be fucked up ngl, 
    #has to use conmat for dof numbers as well as i assuming k global list has same order as conmat, or just element number info i ?
    for i in range(len(k_global_piece_list)):
        current_dof_indices=np.array([np.array(['NDOF per EL?'])])+("conmat[element][Both Nodes]")#somehow has to make list of global DOF indexes iterible by element number order
        #list(Local 0 DOFS, Local 1 DOFS) 
        
        Global_K[np.ix_(current_dof_indices, current_dof_indices)] += k_global_piece_list[i]#does current DOF indices have to be a list split between nodes to allocate non zero k global conts?
        #to     

  

    return Global_K

def do_all_the_shit(El_type_list,n_dof_per_el,Theta_list,n_dof_per_node,Force,active_DOF,total_DOF):
    Local_stiffnesses=local_stiff_list(El_type_list,n_dof_per_el)
    for idx, mat in enumerate(Local_stiffnesses):
        print(f"\nLocal stiffness matrix {idx}:")
        print(mat)
    Global_pieces=Make_Global_piece_list(El_type_list,Local_stiffnesses,Theta_list,n_dof_per_el)
    for idx, mat in enumerate(Global_pieces):
        print(f"\nGlobal stiffness piece {idx}:")
        print(mat)
    Global_k=assemble_global_stiffness_matrix(Global_pieces,Global_k,n_dof_per_node)
    full_disp=solve_system(Global_k,Force,active_DOF,total_DOF)
    return Global_k,full_disp

def data_frame_display(full_disp,Forces):#from old project, just names stuff
    Disp_names=['Endmill tip x','Endmill tip y','Endmill tip theta',
                'Spindle tip x','Spindle tip y','Spindle tip theta',
                'Head tip x','Head tip y','Head tip theta',
                'Column tip x','Column tip y','Column tip theta',
                'Base mid x',' Base mid mid y',' Base mid theta',
                'Base far x',' Base far y',' Base far theta',
                'Base close x',' Base close y',' Base close theta']
    df = pd.DataFrame(full_disp,Disp_names)
    print(df)

    Force_Names=['Endmill tip Fx','Endmill tip Fy','Endmill tip M',
            'Spindle tip Fx','Spindle tip Fy','Spindle tip M',
                'Head tip Fx','Head tip Fy','Head tip M',
                'Column tip Fx','Column tip Fy','Column tip M',
                'Base mid Fx',' Base mid  Fy',' Base mid M',
                'Base far Fx',' Base far Fy',' Base far M',
                'Base close Fx',' Base close Fy',' Base close M']
    df=pd.DataFrame(Forces,Force_Names)
    print(df)


# #func call block
# pick_T_mat (N_DOF_G_PER_ELEMENT,theta)
# local_stiff_list(el_type_list,N_DOF_G_PER_ELEMENT)
# Global_stiff_piece_generator(Local_stiffness_mat,theta,N_DOF_G_PER_ELEMENT)
# Make_Global_piece_list(el_type_list,Local_stiffness_mat_list,theta_list,N_DOF_G_PER_ELEMENT)
# assemble_global_stiffness_matrix(k_global_piece_list, Global_K,N_DOF_per_node)
# solve_system(Global_K, Load_External_list, active_DOF,Tot_DOF)
# do_all_the_shit()
# data_frame_display()

