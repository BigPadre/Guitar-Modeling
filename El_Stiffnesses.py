import numpy as np
import pandas as pd
#12 dof/el
def frame_stiffness_3d(E,G,A,Iy,Iz,J,L):

    #6 DOF per node, 2 nodes, 3 trans 3 rot
    k_quad_1 = np.zeros((6, 6))
    k_quad_1[0, 0] = E * A / L
    k_quad_1[1, 1] = 12 * E * Iz / L**3
    k_quad_1[2, 2] = 12 * E * Iy / L**3
    k_quad_1[3, 3] = G * J / L
    k_quad_1[4, 4] = 4*E * Iy / L
    k_quad_1[5, 5] = 4*E * Iz / L

    k_quad_1[1, 5] = 6 * E * Iz / L**2
    k_quad_1[5, 1] = 6 * E * Iz / L**2
    k_quad_1[2, 4] = -6 * E * Iy / L**2
    k_quad_1[4, 2] = -6 * E * Iy / L**2
    
    k_quad_4=k_quad_1.copy()
    k_quad_4[1, 5] = -6 * E * Iz / L**2
    k_quad_4[5, 1] = -6 * E * Iz / L**2
    k_quad_4[2, 4] = 6 * E * Iy / L**2
    k_quad_4[4, 2] = 6 * E * Iy / L**2

    k_quad_2=np.zeros((6, 6))
    k_quad_2[0, 0] = -E * A / L
    k_quad_2[1, 1] = -12 * E * Iz / L**3
    k_quad_2[2, 2] = -12 * E * Iy / L**3
    k_quad_2[3, 3] = -G * J / L
    k_quad_2[4, 4] = 2*E * Iy / L
    k_quad_2[5, 5] = 2*E * Iz / L

    k_quad_2[1, 5] = 6 * E * Iz / L**2
    k_quad_2[5, 1] = -6 * E * Iz / L**2
    k_quad_2[2, 4] = -6 * E * Iy / L**2
    k_quad_2[4, 2] = 6 * E * Iy / L**2
    k_quad_3=k_quad_2.copy()
    k_quad_3[1, 5] = -6 * E * Iz / L**2
    k_quad_3[5, 1] = 6 * E * Iz / L**2
    k_quad_3[2, 4] = -6 * E * Iy / L**2
    k_quad_3[4, 2] = 6 * E * Iy / L**2

    k_frame = np.zeros((12, 12))
    k_frame[:6, :6] = k_quad_1
    k_frame[6:12, 6:12] = k_quad_4
    k_frame[6:12, :6] = k_quad_3
    k_frame[:6, 6:12] = k_quad_2
    return k_frame
#2 or 4 dof/el
def spring_stiffness_matrix(k,N_DOF_G_PER_ELEMENT):
    if N_DOF_G_PER_ELEMENT==2:
        local_spring_stiffness_N_GDOF = np.array([[k, -k], [-k, k]])
    if N_DOF_G_PER_ELEMENT==4:
        local_spring_stiffness_N_GDOF = np.zeros((4, 4))
        local_spring_stiffness_N_GDOF[0, 0] = k
        local_spring_stiffness_N_GDOF[0, 2] = -k
        local_spring_stiffness_N_GDOF[2, 0] = -k
        local_spring_stiffness_N_GDOF[2, 2] = k
    return local_spring_stiffness_N_GDOF
#2 or 4 dof/el
def truss_stiffness_matrix(L, E, A,N_DOF_G_PER_ELEMENT):
    k=(E * A / L)
    if N_DOF_G_PER_ELEMENT==2:
        local_truss_stiffness_N_GDOF = np.array([[k, -k], [-k, k]])
    if N_DOF_G_PER_ELEMENT==4:
        local_truss_stiffness_N_GDOF = np.zeros((4, 4))
        local_truss_stiffness_N_GDOF[0, 0] = k
        local_truss_stiffness_N_GDOF[0, 2] = -k
        local_truss_stiffness_N_GDOF[2, 0] = -k
        local_truss_stiffness_N_GDOF[2, 2] = k
    return local_truss_stiffness_N_GDOF
#6 or 4 dof/el
def beam_stiffness_matrix(L, E, I,A,N_DOF_G_PER_ELEMENT):
    # Local stiffness matrix for a 2D beam element with 6 DOF (2 translations and 1 rotation per node)
    c1=A*E/L
    c2=E*I/L**3
    if N_DOF_G_PER_ELEMENT==6:
        k_local_beam = np.array([
        [c1, 0, 0, -c1, 0, 0],
        [0, 12*c2, 6*c2*L, 0, -12*c2, 6*c2*L],
        [0, 6*c2*L, 4*c2*L**2, 0, -6*c2*L, 2*c2*L**2],
        [-c1, 0, 0, c1, 0, 0],
        [0, -12*c2, -6*c2*L, 0, 12*c2, -6*c2*L],
        [0, 6*c2*L, 2*c2*L**2, 0, -6*c2*L, 4*c2*L**2]
    ])
    elif N_DOF_G_PER_ELEMENT==4:
        k_local_beam=np.array([[12*c2, 6*c2*L,-12*c2, 6*c2],
                               [6*c2*L, 4*c2*L**2,-6*c2*L, 2*c2*L**2],
                               [-12*c2, -6*c2*L,12*c2, -6*c2],
                               [6*c2*L, 2*c2*L**2,-6*c2*L, 4*c2*L**2]])
    return k_local_beam

