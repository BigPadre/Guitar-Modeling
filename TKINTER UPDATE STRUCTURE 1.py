import tkinter as tk

def custom_loop():
    # Place your code logic here
    print("Custom loop running...")
    root.update()  # Refresh the Tkinter window
    root.after(100, custom_loop)  # Continue the custom loop

root = tk.Tk()
root.after(100, custom_loop)  # Start the loop
root.mainloop()

