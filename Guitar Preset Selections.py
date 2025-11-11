from tkinter import *
# Function to display the selected option
def show_selection():
   label.config(text=f"Selected: {selected_option.get()}")


Violin_Family_Options=["Electric Violin","Electric Viola","Electric Cello","Electric Upright Bass"]
Violin_Standard_Tunings=["Standard GDAE", "Baroque Tuning", "Scordatura"]
Guitar_Family_Options=["Electric Guitar","Electric Bass Guitar","Electric Slide Guitar","Electric Ukelele"]
Guitar_Standard_Tunings=["Standard E", "Drop D", "DADGAD"]
def Instrument_Type_Options_Dropdown():
    # Dropdown options
   
    
    Instrument_Type_Options=[]
    for option in Guitar_Family_Options:
        Instrument_Type_Options.append(option)
    for option in Violin_Family_Options:
        Instrument_Type_Options.append(option)
    Instrument_Type_Options.append("Custom Instrument")
    # Initialize a selected option
    selected_option = StringVar(value="")

    # Create dropdown menu and insert into window
    
    Instrument_Type_Options_Dropdown=OptionMenu(root, selected_option, *Instrument_Type_Options)

    Instrument_Type_Options_Dropdown.pack()

    # Button to display the selection for testing?
    Button(root, text="Show Selection", command=show_selection).pack()

    # Initialize label below selection 
    label = Label(root, text="")
    label.pack()
    return selected_option
def Scale_Length_Options_Dropdown():
    # Dropdown options
    Scale_Length_Options=[""]
    # Initialize a selected option
    selected_option = StringVar(value="")

    # Create dropdown menu and insert into window
    Scale_Length_Options_Dropdown=OptionMenu(root, selected_option, *Scale_Length_Options)

    Scale_Length_Options_Dropdown.pack()

    # Button to display the selection for testing?
    Button(root, text="Show Selection", command=show_selection).pack()

    # Initialize label below selection 
    label = Label(root, text="")
    label.pack()
    return selected_option
def Number_of_Frets_Options_Dropdown():
    # Dropdown options
    Number_of_Frets_Options=[""]
    # Initialize a selected option
    selected_option = StringVar(value="")

    # Create dropdown menu and insert into window
    Number_of_Frets_Options_Dropdown=OptionMenu(root, selected_option, *Number_of_Frets_Options)

    Number_of_Frets_Options_Dropdown.pack()

    # Button to display the selection for testing?
    Button(root, text="Show Selection", command=show_selection).pack()

    # Initialize label below selection 
    label = Label(root, text="")
    label.pack()
    return selected_option
def Number_of_Strings_Options_Dropdown():
    # Dropdown options
    Number_of_Strings_Options=[""]
    # Initialize a selected option
    selected_option = StringVar(value="")

    # Create dropdown menu and insert into window
    Number_of_Strings_Options_Dropdown=OptionMenu(root, selected_option, *Number_of_Strings_Options)

    Number_of_Strings_Options_Dropdown.pack()

    # Button to display the selection for testing?
    Button(root, text="Show Selection", command=show_selection).pack()

    # Initialize label below selection 
    label = Label(root, text="")
    label.pack()
    return selected_option
def Action_Spec_Options_Dropdown():
    # Dropdown options
    Action_Spec_Options=[""]
    # Initialize a selected option
    selected_option = StringVar(value="")

    # Create dropdown menu and insert into window
    Action_Spec_Options_Dropdown=OptionMenu(root, selected_option, *Action_Spec_Options)

    Action_Spec_Options_Dropdown.pack()

    # Button to display the selection for testing?
    Button(root, text="Show Selection", command=show_selection).pack()

    # Initialize label below selection 
    label = Label(root, text="")
    label.pack()
    return selected_option

#Still doesnt work lmao Violin_Standard_Tunings=["Standard GDAE", "Baroque Tuning", "Scordatura"]
def Tuning_Options_Dropdown(Selected_Instrument):
    # Dropdown options
    Tuning_Options=[]
    selected_option = StringVar(value="")
    if Selected_Instrument.get() in Violin_Family_Options:
        for option in Violin_Standard_Tunings:
            Tuning_Options.append(option)
    if Selected_Instrument.get() in Guitar_Family_Options:
        for option in Guitar_Standard_Tunings:
            Tuning_Options.append(option)
    Tuning_Options.append("Custom Tuning")
    # Initialize a selected option
    selected_option = StringVar(value="")

    # Create dropdown menu and insert into window
    Tuning_Options_Dropdown=OptionMenu(root, selected_option, *Tuning_Options)

    Tuning_Options_Dropdown.pack()

    # Button to display the selection for testing?
    Button(root, text="Show Selection", command=show_selection).pack()

    # Initialize label below selection 
    label = Label(root, text="")
    label.pack()
    return selected_option

# Create the main window
root = Tk()
# root.geometry("200x200")
Selected_Tuning=[]


label=Label(root, text="Select Instrument Type:")
label.pack()
Selected_Instrument=Instrument_Type_Options_Dropdown()
label=Label(root, text="Select Scale Length:")
label.pack()
Selected_Scale_Length=Scale_Length_Options_Dropdown()
label=Label(root, text="Select Number of Frets:")
label.pack()
Selected_Number_of_Frets=Number_of_Frets_Options_Dropdown()
label=Label(root, text="Select Number of Strings:")
label.pack()
Selected_Number_of_Strings=Number_of_Strings_Options_Dropdown()
label=Label(root, text="Select Action Specification:")
label.pack()
Selected_Action_Spec=Action_Spec_Options_Dropdown()
label=Label(root, text="Select Tuning:")
label.pack()
# Tuning selection based on instrument type selection
# doesn't work yet, how do you have the dropdown update based on prior selection?
Selected_Tuning=Tuning_Options_Dropdown(Selected_Instrument)





label.pack()
root.mainloop()