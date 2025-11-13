import tkinter as tk
import threading

def run_in_background():
    for i in range(10):
        print(f"Background task running: {i}")

class App(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.start()

    def run(self):
        root = tk.Tk()
        button = tk.Button(root, text="Start Task", command=run_in_background)
        button.pack()
        root.mainloop()

if __name__ == "__main__":
    app = App()