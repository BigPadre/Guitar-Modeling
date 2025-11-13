# Guitar-Modeling
hopefully a helpful tool to simulate guitars based on whatever choices can be predicted

takes strings, tunings, an geometry info to predict if what you build ends up being how you'd prefer

also hopefully can improve accuracy to reality by feeding it more geometry info

will also look at deformation of a real object to reccomend modifications to geometry or material choice with user preferences as the standard (action at certain frets, limits on neck size, etc...)

# TO DO: 
- Create central database for presets
- Figure out how to have app that updates based on high level selections
    - based on classes of objects that hold high level or geometry info for specfic aspects/parts
    - high level info must be selected before geometry info
    - possible update loop/persistence to allow for quick changes before/concurrently with fea module 
- Figure out how to save and or export high level selections
- Figure out how to save and or export geometry level selections
- Figure out how to pass info to FEA module
