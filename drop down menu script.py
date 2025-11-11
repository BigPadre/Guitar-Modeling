from tkinter import *
# Function to display the selected option
def show_selection():
   label.config(text=f"Selected: {selected_option.get()}")

# Create the main window
root = Tk()
root.geometry("200x200")

# Dropdown options
options = ["Option 1", "Option 2", "Option 3"]


# Initialize a selected option
selected_option = StringVar(value="Option 1")

# Create dropdown menu and insert into window
dropdown = OptionMenu(root, selected_option, *options)
dropdown.pack()

# Button to display the selection for testing?
Button(root, text="Show Selection", command=show_selection).pack()

# Initialize label below selection 
label = Label(root, text="")
label.pack()
root.mainloop()