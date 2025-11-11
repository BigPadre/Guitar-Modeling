import numpy as np
import pandas as pd



fret_ns=np.arange(1,14)
n_frets_meas=len(fret_ns)
cm_indexes=np.arange(6)#0 indeixing
Scale_len=30#inches

stock_len=20#inches



def calculate_area_moment_of_inertia(points, check_simple=True):#not fully tested
    """
    Calculate the area moments of inertia (Ix, Iy) and product moment (Ixy)
    for a simple polygon defined by an ordered list of vertices.

    Inputs/outputs (contract):
    - points: iterable of (x, y) tuples or array-like. Vertices must be ordered
      consistently (CW or CCW). The polygon is assumed to be simple (no
      self-intersections) and edges are straight between consecutive vertices.
    - Returns: (Ix_c, Iy_c, Ixy_c) moments about the polygon centroidal axes.

    Notes:
    - Units are the units of coordinates squared times area (if coords in mm,
      moments are mm^4). Keep coordinates consistent.
    - The implementation uses the shoelace-based line-integral formulas.
    - If the polygon orientation is clockwise the computed signed area will be
      negative; the formulas below handle the sign consistently without using
      abs() on the integrals (which can mask orientation bugs).
    """
    pts = np.asarray(points, dtype=float)#points has correct amount, but this adds on another point somehow
    if pts.ndim != 2 or pts.shape[1] != 2:
        raise ValueError("points must be an iterable of (x, y) pairs")

    n = pts.shape[0]
    if n < 3:
        raise ValueError("At least 3 points are required to define a polygon.")

    # # Close polygon if not already closed
    if not np.allclose(pts[0], pts[-1]):
         pts = np.vstack([pts, pts[0]])#this might fuck it up? adds on first el to close...
    #if commented out, first fret can't even be completely processed
    #add vertexes at bottom left and right corners to clse polygon instead of whatever tf that was
    add_points=[(0,0),(pts[-1,0],0)]
    pts=np.insert(pts,0,add_points[0])
    pts=np.insert(pts,-1,add_points[1])
    # Accumulators (signed values)
    A2 = 0.0      # 2*A (signed)
    Cx6 = 0.0     # 6*A*Cx
    Cy6 = 0.0     # 6*A*Cy
    Ix_raw = 0.0  # 12*Ix (raw integral)
    Iy_raw = 0.0  # 12*Iy
    Ixy_raw = 0.0 # 24*Ixy

    for i in range(n):
        x0, y0 = pts[i],pts[i + 1]#had to change indexes due to format of pts, but seems to chug in some kinda way
        x1, y1 = pts[i + 2],pts[i+3]
        #prev:
        #pts has 2 0,21 points making the ordering fucked, making opposite sign cont
        cross = x0 * y1 - x1 * y0  # shoelace term

        A2 += cross
        #prev
        #cross ends up cancelling A2 sum, making for zero area of 11th fret specifically...
        Cx6 += (x0 + x1) * cross
        Cy6 += (y0 + y1) * cross

        Ix_raw += (y0 * y0 + y0 * y1 + y1 * y1) * cross
        Iy_raw += (x0 * x0 + x0 * x1 + x1 * x1) * cross
        Ixy_raw += (x0 * y1 + 2 * x0 * y0 + 2 * x1 * y1 + x1 * y0) * cross

    A = 0.5 * A2
    if abs(A) < 1e-12:
        raise ValueError("Polygon area is zero (degenerate polygon)")
    #n should be 4 with the fuckd up random addition to close shape but is somehow 3
    #zeroing happpens at i=2nd point
    #program takes upper verticies but lacks the bottom right and left corners
        #bot right should be same x val as max, y val is 0
        #bot left val same as min x val, y val 0

    Cx = Cx6 / (6.0 * A)
    Cy = Cy6 / (6.0 * A)

    # raw integrals scaled back to standard values
    Ix = Ix_raw / 12.0
    Iy = Iy_raw / 12.0
    Ixy = Ixy_raw / 24.0

    # Move to centroidal axes (parallel axis theorem)
    Ix_c = Ix - A * Cy * Cy
    Iy_c = Iy - A * Cx * Cx
    Ixy_c = Ixy - A * Cx * Cy

    # Optionally check for simple polygon (basic winding/self-intersection
    # check). This is a light-weight test to catch obvious problems.
    if check_simple:
        # If area sign is negative, vertices were given in clockwise order.
        # That's fine; we return positive centroidal moments. We don't take
        # absolute of integrals directly because that would hide bugs.
        # A more thorough self-intersection check can be added if needed.
        pass

    return float(Ix_c), float(Iy_c), float(Ixy_c)

def scale_len_fret_locs(scale_len,stock_len):
    if scale_len==30:#inch
        fret_loc_data=[
        1.683785149,
        3.273065884,
        4.773146375,
        6.189033092,
        7.525451507,
        8.786861873,
        9.977474105,
        11.10126183,
        12.16197565,
        13.16315567,
        14.10814328,
        15.00009236,
        15.84197975,
        16.63661523,
        17.38665085,
        18.09458985,
        18.76279495,
        19.39349624,
        19.9887987,
        20.5506891,
        21.08104274,
        21.58162967
        ]#inches for 30" scale length, 21 frets
    else:
        print("scale length bruh")
    if fret_loc_data[-1]>stock_len:#checks if last fret is out of stock length
        for i in range(len(fret_loc_data)):#if so for every data point in fret loc data original
            if fret_loc_data[i]>stock_len:#if that data point is out of stock length
                fret_loc_data=fret_loc_data[:i]#cut the list off there
                break

        print("all frets fit in stock length")
        max_Frets=len(fret_loc_data)
    return fret_loc_data, max_Frets

def generate_thickness_data(max_Frets,cm_indexes):
    #neck data for each fret and cm index
    #rows=cm indexes
    #cols=fret positions
    #data in mm
    Neck_Data=[] 
    zero_data,one_data,two_data,three_data,four_data,five_data=[None]*max_Frets,[None]*max_Frets,[None]*max_Frets,[None]*max_Frets,[None]*max_Frets,[None]*max_Frets   
    #All cm
    #should be user input somehow but hardcoded for now
    zero_fret_indexes=[0,1,2,3,4,5,6,7,8,9,10,11,12,13]#all frets measured up to 14
    one_fret_indexes=[0,2,5,6,8]#not all measured
    two_fret_indexes=[]#no frets measured
    three_fret_indexes=[0,1,2,3,4,5,6,7,8,9,10,11,12,13]#same as zero
    four_fret_indexes=[]#no frets measured
    five_fret_indexes=[0,1,2,3,4,5,6,7,8,9,10,11,12,13]#same as zero
    
    one_data_act=[15.45,15.25,15.35,17,19.3]/10
    zero_data_act=[14.25,13,12.3,11.3,11.3,12.3,13.2,15.15,16.175,18,20.25,21,21.05,21]/10
    three_data_act=21/10 #pop with all 21 
    four_data_act=[None]/10#no data
    two_data_act=[None]/10#no data
    five_data_act=[20,20,20,20,20,21,21,21,21,21,21,21,21.5,21.5]/10      
    #populate data lists with actual data at correct indexes
    count=0
    for i in one_fret_indexes:
        one_data[i]=one_data_act[count]
        count+=1
    count=0
    for i in five_fret_indexes:
        
        five_data[i]=five_data_act[count]
        count+=1
    count=0
    for i in zero_fret_indexes:
        
        zero_data[i]=zero_data_act[count]
        count+=1
    count=0
    for i in three_fret_indexes:
        
        three_data[i]=three_data_act
        count+=1
    count=0
    for i in four_fret_indexes:
        
        four_data[i]=four_data_act[count]
        count+=1
    count=0
    for i in two_fret_indexes:

        two_data[i]=two_data_act[count]
        count+=1
    Neck_Data=[zero_data,one_data,two_data,three_data,four_data,five_data]

    return Neck_Data

def calc_areas(polygon_points):#not fully tested 
    area=0
    for i in range(len(polygon_points)-1):
        x0, y0 = polygon_points[i]
        x1, y1 = polygon_points[i + 1]
        area += x0 * y1 - x1 * y0
    return abs(area) / 2.0

def generate_neck_mesh(n_frets_meas,cm_indexes,Neck_Data,fret_locs):
    act_neck_data=[]
    for k in range(n_frets_meas):#for each fret
        current_loc=fret_locs[k]#get fret loc
        for i in cm_indexes:#for each cm index of each fret
            current_cm_index=cm_indexes[i]#get cm index
            current_cm_data=Neck_Data[i]#get data of all frets for that cm index
            current_thicc=current_cm_data[k]#get thicc data for current fret
            if current_thicc is None:
                pass
            else:
                act_neck_data.append([(current_loc,current_cm_index,current_thicc)])  
    return act_neck_data

def generate_geom_param_lists(n_frets_meas,fret_locs,neck_geom_mesh):
    fret_mois = []
    fret_mois_polar=[]
    fret_areas=[]
    for fret in range(n_frets_meas):

        current_fret_loc = fret_locs[fret]
        cxn_coords = [(item[0][1],item[0][2]) for item in neck_geom_mesh
                    if np.isclose(item[0][0], current_fret_loc)]#gives 5 thicknesses so it might actually work?
        
        # current_fret_loc = fret_locs[fret]
        # current_fret_data_ind=np.where(neck_geom_mesh[:][:][0]==current_fret_loc)#indexing this shit is so dumb 
        
    #calculate area moment of inertia
        current_fret_moi = calculate_area_moment_of_inertia(cxn_coords)
        current_fret_moi_polar=polar_moment_of_inertia(cxn_coords)
        current_fret_area=calc_areas(cxn_coords)
        fret_mois.append([current_fret_moi])
        fret_mois_polar.append([current_fret_moi_polar])
        fret_areas.append([current_fret_area])
    #Ix and Iy (0,1) important for bending stiffness, no idea wtf Ixy represents
    #Signs need to be scrubbed (though Ixy has some pos...)
    return fret_mois,fret_mois_polar,fret_areas

def polar_moment_of_inertia(vertices):#not fully tested
    """
    Calculate the polar moment of inertia of a polygon about the origin.
    
    Parameters:
        vertices (list of tuples): List of (x, y) coordinates of the polygon vertices in order.
                                   The polygon should be closed (first and last vertices should match).
    
    Returns:
        float: Polar moment of inertia.
    """
    n = len(vertices)
    if n < 3:
        raise ValueError("A polygon must have at least 3 vertices.")
    
    J = 0  # Polar moment of inertia
    for i in range(n - 1):
        x0, y0 = vertices[i]
        x1, y1 = vertices[i + 1]
        common_term = (x0 * y1 - x1 * y0)
        J += (x0**2 + x0 * x1 + x1**2 + y0**2 + y0 * y1 + y1**2) * common_term
    
    J = abs(J) / 12.0
    return J

def generate_spline_curve(): #unfinished
    #takes thickness vals and their cm indexes per fret cross section 
    #generates spline curve for thickness along neck width
    #returns one fitted curve per fret cross section to use in other prop calc funcs
    cubic_splines=[]
    
    for j in range(max_Frets):
        thickness_vals=[]
        
        thickness_vals.append(Neck_Data[:][j])#gets thickness data for current fret cross section
    
        cs=interp.CubicSpline(cm_indexes,thickness_vals[i],bc_type='natural')
        cubic_splines.append(cs)
    return cubic_splines
    




# df0=pd.DataFrame(fret_mois)
# df1=pd.DataFrame(fret_mois_polar)
# print(df0,df1)

'''
polygon_points = [(0, 0), ()] 
Ix, Iy, Ixy = calculate_area_moment_of_inertia(polygon_points)
print(f"Ix: {Ix}, Iy: {Iy}, Ixy: {Ixy}")
'''

#array of nones that you can progressively fill with more fret/neck data to poly fit?
#((L-Prev)/17.817)+Prev
#counted considred from 1 to 14 or whatever the largest in table is rn, 
# 0 fret pretty much only in one place if desired

# for n in range(1,n_frets_meas):
#     fret_pos=fret_loc_data[n-1]
#     if fret_pos>stock_len:
#         max_Frets=n-1
#         break
#     else:
#         max_Frets=n_frets_meas

#x=fret pos
#y=cm index
# z=thicc

#Neck_Data[0] = [width, thickness, x_offset, y_offset]#what is this 


#Nones later become nans, probably will be a problem def a problem
# this func no likey bc its not a list of tuples [(x,y),(x,y)... Fixed????

# def generate_polygon_segments(Neck_Data,cm_indexes,max_Frets):
    
#     #for each fret, get the points and make tuple with namesake
#     polygon_points = []
#     for j in range(len(cm_indexes)):
#         for i in range(len(Neck_Data[j])):#for each fret

#             thicc=Neck_Data[j][i]#mm
#             # Append points to the polygon list in order #[x (cm),ys(h on cm line)...]
#             polygon_points.extend([(j,thicc)])
#         #filter out Nones
#         # polygon_points = [pt for pt in polygon_points if pt[1] is not None]
#         # Close the polygon by adding the first point at the end?
#         # polygon_points.append(polygon_points[0])?????
#     return polygon_points

# polygon_points=generate_polygon_segments(Neck_Data,cm_indexes,max_Frets)
#loop over each cm index and interpolate between to get points for all frets?
    #get fret locs for each cm index point measured
    #establish mesh of global coords based on fret locs and cm index
    #populate mesh with known thickness data
        #need to get list of measured frets and cm indexes per fret 
        #list: 1-13 frets 
            #cm 0 has all frets 
        #max frets is 19 but frets meas is 13
        #some are len 13 but some are len 19 bruhhh
        #0:13
        #1:19
        #2:19
        #3:19
        #4:19
        #5:14 oops
        #steps: 
            #1: make all lists len 19 Done
            #2: populate with known data, cut off after frets in stock length Done?
            #3: interpolate missing data per fret to make full profile
                #get actual arc len per fret for accuaracy?

#splitting up data into segments per fret
    #determine which frets have what cm index data
    #get list of tuples of (fret_n,cm index,thicc) for each fret
        #mesh of points to interpolate between 
        #can also create other mesh of areas/moments of inertia
    #return graphs of thickness vs cm index for each cross section


# for point in polygon_points:
#     for i in range(len(cm_indexes)):
#     #check if data first val matches cm index val
#         if point[0] == cm_indexes[i]:#hopefully indexing tuple correct lol

    # Ix, Iy, Ixy = calculate_area_moment_of_inertia(polygon_points)
    # A_list=calc_areas(polygon_points)
# print(f"Ix: {Ix}, Iy: {Iy}, Ixy: {Ixy}, {fret_locs} frets, {A_list} mm^2 area")
#negative Ix and Iy...
#might be due to point ordering? 
#might be due to non centroid reference?
#doesn't come out as a list of I's 

#calculate area moment of inertia as a function of fret location 
    #get all thicc(cm_range)|current_fret_loc
        #calc each MOI based on thicc points in fret 
            #will have to be ordered either cw or ccw, mag may or may not be the same...