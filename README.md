# Guitar-Modeling
hopefully a helpful tool to simulate guitars based on whatever choices can be predicted

takes strings, tunings, an geometry info to predict if what you build ends up being how you'd prefer

also hopefully can improve accuracy to reality by feeding it more geometry info

will also look at deformation of a real object to reccomend modifications to geometry or material choice with user preferences as the standard (action at certain frets, limits on neck size, etc...)

# Current Organization:

Main Branch: preliminary versions of scripts before being finalized

Prelim Assembly Branch off of main is most finalized assembly of code

Stability Data Branch: branch containing most up to date data sets/stats for measured instrument stability 

# Info Input Modules
Highest Level Info: 
- Instrument family, number of strings, frets or not, desired tunings to simulate
    - Mostly to narrow down common preset design choices
Material Info:
- Hardware mats, body component mats, string mats
    - Likely would need some range of props for wishy washy materials like wood
    - Would rely mostly on manufacturer info for strings
    - Type of mats for hardware could be kind of interesting to get accurate info on
  
Geometry info:
- Hardware locations, desired string action, part dims, some relative part dimensions
  - Standard parts like bolts very straight forward to measure accurately, could prelaod
  - Meant to be iterative for the sake of minimizing requried performance/patience to load additional geometry info
  - Ideally persitent record of entered geometry info for particular project, exportable?  
# FEA Module
Options for Element Types Ranked by Gut Feeling Usefulness: 
- 3D polyhedra
    - Nice for mapping large(ish) regions of geometry, essentially all wood components
    - Variety of ways to map/combine shapes for refinement
    - Node count can be quite big, biased refinement likely required
    - Kind of easy to generate meshes based on logical structures/simple geometric subdivisions

- String/Basic Spring El
    - Nice for simple elastic members, essentially only strings would be compatible
    - Members like strings could be affected by creep in addition to macro structure, not focused on that for now
 - 2D/kind of 3D Frame and Beam type Elements:
    - Assumes plane loading/stresses/deformation per element, doesn't work nice with all 3D scenarios
       - Some types can do bendining, axial, and torsional loads
       - Requires engine to calc MOI's for 3 translation, 1 rotation basis as well as area 
    - Can kind of approximate 3D structures by mapping 2D sets of DOF's to global 3D mesh by superposition of orthogonal conts
       - Has both translational and rotational DOF's in all 3 (global) dimensions, 2 nodes per element
       - Not as high resolution as polyhedra, ideal for longer parts loaded predominantly in bending
       - Could be nice to save on node count relative to polyhedra
       - Probably would be kind of a pain?
           - Need to keep track of relative orientation of elements relative to each other as well as relative to global coords (12x12 T matrix)
           - Confirming angles in all 3 principle axes could be kind of a pain measurement wise
           - Somewhat easier to measure geometry to approximate true 3D load orientations
               -Would need nice reference datums/technique for most general applicability 
# General Potential Issues: 
- Measurement quantity needs to be relatively low and or simple to do
    - More willing to compromise on quantity than simplicity
  - Anisotropy (wood especially) might factor into final deformation state beyond what sim can predict
    - Might be possible to quantify divergence from sim/convergence of divergence to get a more concrete idea of how the material really acts
- Fidelity largely based on user dilligence in measurement/knowledge of materials
    - Graphics/pictures could help instruction, would have to be very clear and or somewhat interactive
- Hardware dynamics kind of tricky to guaruntee
  - Backlash and fixturing could throw off accuracy while not being terribly obvious
    - Track rotation of pegs to quantify?
      - Might need string pitch info to track structural effects versus effects of fixtures/internal mechanism slop
      - Use phone app/clip on tuners for a start? No idea the freq resolution on those lol
# TO DO: 
- Create central database for presets
    - Got some string tension excel from a forum, did some calcs to get a tension range
    - prev online calc predicted half the tension given the same gague and note, calced fundamentals based on table tensions but they were consistently larger than target notes
      - Measured mass/lenght of strings, referenced note frequency equivalents
        - Only could register 6th and 5th mass
      - Solving for fundamental using lower tension assumption by scaling the original by the sqrt of tension ratio, fundamentals come into far better agreement
- Figure out how to have app that updates based on high level selections
    - based on classes of objects that hold high level or geometry info for specfic aspects/parts
    - high level info must be selected before geometry info
    - possible update loop/persistence to allow for quick changes before/concurrently with fea module 
- Figure out how to save and or export high level selections
- Figure out how to save and or export geometry level selections
- Figure out how to pass info to FEA module
- 
      - Neck Polygon Processing submodule confirmed generating geom params for fb region
  
          -Need to integrate head+heel dims for compactness
  
      - Need submodule for FEA sim data interfaces
  
          - Accepts geom props from Neck Polygon Processing
  
              - Other joints/major parts will be structured like Neck Poly, classes assembled together
  
          - Need additional material props submodule
