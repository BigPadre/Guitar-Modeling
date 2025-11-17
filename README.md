# Guitar-Modeling
hopefully a helpful tool to simulate guitars based on whatever choices can be predicted

takes strings, tunings, an geometry info to predict if what you build ends up being how you'd prefer

also hopefully can improve accuracy to reality by feeding it more geometry info

will also look at deformation of a real object to reccomend modifications to geometry or material choice with user preferences as the standard (action at certain frets, limits on neck size, etc...)

# Info Input Modules

# FEA Module
Options for Element Types Ranked by Gut Feeling Usefulness: 
- 3D polyhedra
    - Nice for mapping large(ish) regions of geometry, essentially all wood components
    - Variety of ways to map/combine shapes for refinement
    - Node count can be quite big, biased refinement likely required
    - Kind of easy to generate meshes based on logical structures/simple geometric subdivisions
    - Anisotropy (wood especially) might factor into final deformation state beyond what sim can predict
      - Might be possible to quantify divergence from sim/convergence of divergence to get a more concrete idea of how the material really acts
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
 
# TO DO: 
- Create central database for presets
- Figure out how to have app that updates based on high level selections
    - based on classes of objects that hold high level or geometry info for specfic aspects/parts
    - high level info must be selected before geometry info
    - possible update loop/persistence to allow for quick changes before/concurrently with fea module 
- Figure out how to save and or export high level selections
- Figure out how to save and or export geometry level selections
- Figure out how to pass info to FEA module
