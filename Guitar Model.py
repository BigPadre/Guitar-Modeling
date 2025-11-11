'''
#theoretical flow:
#0. Create deflection mesh out of measurements per span
#1. Establish mat and geom props per el thru scripts
#2. populate local stiffnesses script w/props
#3. Mult by global stiffness to find total force developed pernodes
#4. Advise step...
    #4a. determine limit on actions 
    #4b. determine deviation of action
    #4c. Element by element, solve for change in each parameter to meet or otherwise approach
    #action spec
    #4d. Output delta params in order from least to most change necessary 

    #Params: MOI,E,L,A,J,
        #eval criteria:
            #equivalent scaling factor
                #E: mat based decision 
                #A/L/J/MOI: naive geom adjustment 
            #specific mag of change reccomendation  (mostly L)
                #considers scale len and other constraints?


'''
#FEA Approximation of Guitar Assembly
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.tri as mtri
import Mesh_Info_Script,El_Stiffnesses,Geom_Prop_Script,System_Solve_Script,String_Prop_Script
from Mesh_Info_Script import E_body,E_maple,E_neck,E_pine,El_type_list,total_DOF,Theta_list,A_list,L_list,I_list
from El_Stiffnesses import frame_stiffness_3d
from System_Solve_Script import assemble_global_stiffness_matrix,data_frame_display,do_all_the_shit,Global_stiff_piece_generator,Make_Global_piece_list,local_stiff_list,pick_T_mat,solve_system


# #0: establish defl state of real guitar per fret 


#1: Mesh and geom props for theoretical stiffness props
#Geom info
fret_locs,max_Frets=Geom_Prop_Script.scale_len_fret_locs(Geom_Prop_Script.Scale_len,Geom_Prop_Script.stock_len)#max frets works but i measured 5 less?
Neck_Data=Geom_Prop_Script.generate_thickness_data(max_Frets,Geom_Prop_Script.cm_indexes)#works
neck_geom_mesh=Geom_Prop_Script.generate_neck_mesh(Geom_Prop_Script.n_frets_meas,Geom_Prop_Script.cm_indexes,Neck_Data,fret_locs)#pog as fuck this shit actually works [loc, cm, thicc]
fret_mois,fret_mois_polar,fret_areas=Geom_Prop_Script.generate_geom_param_lists(Geom_Prop_Script.n_frets_meas,fret_locs,neck_geom_mesh)



# #2: populate stiffnesses using syst solve

#To do: 
#check NDOF PER NODE for list array compatibility 

#3: Find Internal Loads using #2
#To Do:

#4: Take user preferences for deflection specs, string choice, tuning to optimize each element or set of elements 