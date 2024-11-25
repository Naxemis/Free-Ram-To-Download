import tkinter as tk
import time
import threading
import random

# generates random colour in hex system
def generate_random_colour():
        random_colour = lambda: random.randint(0, 255)
        # ":02x" - tells Python to format number as a two-digit hex
        # "0" - ensures that if the hex number has fewer than two digits, it will pad the output with leading zeros.
        # "2" - specifies the width of the output
        # "x" - formats the number as a lowercase hex
        return f"#{random_colour():02x}{random_colour():02x}{random_colour():02x}"

class App:
    def __init__(self, tkinter_root, test_mode):
        self.test_mode = test_mode
        self.root = tkinter_root

        self.root.title("Window") # title of main window

        self.root.resizable(0, 0) # disables min/max button

        # size of main window
        window_width = 512
        window_height = 288
        self.root.geometry(f"{window_width}x{window_height}")

        # button that start process of creating new windows
        self.main_button = tk.Button(self.root, text="Create Windows", command=self.start_creating_windows)
        self.main_button.pack()

    def start_creating_windows(self):
        threading.Thread(target=self.create_multiple_windows).start()

    def create_multiple_windows(self):
        if self.test_mode == False: # if test_mode is disabled - constantly create windows after clicking button once
            while True:
                self.create_new_window()
                time.sleep(0.01)
        else: # if test_mode is enabled - create only 10 windows per one click on button
            for index in range(10):
                self.create_new_window()
                time.sleep(0.01)

    def create_new_window(self):
        new_window = tk.Toplevel(self.root)

        new_window.title("Window") # title of new window

        new_window.resizable(0, 0) # disables min/max button
        new_window.overrideredirect(True) # makes window frameless

        # size of new window
        window_width = 256
        window_height = 144
        new_window.geometry(f"{window_width}x{window_height}")

        # set random position for new window
        random_x_position = random.randint(0, self.root.winfo_screenwidth() - window_width)
        random_y_position = random.randint(0, self.root.winfo_screenheight() - window_height)
        new_window.geometry(f"{window_width}x{window_height}+{random_x_position}+{random_y_position}")

        # set random colour of background for new window
        random_colour = generate_random_colour()
        new_window.configure(bg=random_colour)

root = tk.Tk()
app = App(root, True)
root.mainloop()
