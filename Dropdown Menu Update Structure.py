import tkinter as tk
import threading
from tkinter import *
#Assigning attributes strucure
    #Construction class determines preset selections for string class and hardware class only
    #main loop of menu window must call update function to refresh string and hardware class attributes based on construction class selections
    #construction selections must occur as first step in loop
    
        #must pull attributes from prepopulated data sets based on construction class selections to then assign to string and hardware classes
    #Neck, Head, Neck Joint, and Body classes hold custom geometry and material selecitons independant of construction class






def Update_Menu_Options():
    #function to update menu options if the functio detects changes in selection options when caled by the run function in the 
    #menu window class
    for i in range(10):
        print(f"Background task running: {i}")
def save_instrument_data(self):
        #function to save current instrument data to file when user selects save option in menu window
        pass
class High_Level_Menu_Window(threading.Thread):
#OBJECT CLASS FOR HIGH LEVEL SELECTIONS OF INSTRUMENT TRAITS BASED ON CUSTOM OR PRESET INPUTS
    #INTIALLY ASKS FOR INSTRUMENT CONSTRUCTION CLASS INFO TO PULL PRESET DATA FOR STRINGS AND HARDWARE INTO THEIR RESPECTIVE DROPDOWNS
        #DROPDOWNS FOR HIGH LEVEL INFO POPULATE CLASS INFO FOR STRINGS AND HARDWARE OBJECT CLASSES  
    def __init__(self):
        threading.Thread.__init__(self)
        self.start()
    
    def run(self):
        root = tk.Tk()
        Instrument_Type_Options_Dropdown=OptionMenu(root, selected_option, *Instrument_Type_Options)

        Instrument_Type_Options_Dropdown.pack()

        button = tk.Button(root, text="Select Instrument Type", command=Update_Menu_Options)
        button.pack()
        root.mainloop()
        
''' 
#might need to be a threading class as well but idk what that means yet
class Geometry_Menu_Window:
#
class Simulation_Menu_Window:
'''
if __name__ == "__main__":
    app = High_Level_Menu_Window()