import tkinter as tk
import time
import threading
import random

def generate_random_colour():
        random_colour = lambda: random.randint(0, 255)
        return f"#{random_colour():02x}{random_colour():02x}{random_colour():02x}"

class App:
    def __init__(self, tkinter_root):
        self.root = tkinter_root
        self.root.title("Window")

        self.root.resizable(0, 0)

        window_width = 512
        window_height = 288
        self.root.geometry(f"{window_width}x{window_height}")

        self.main_button = tk.Button(self.root, text="Create Windows", command=self.start_creating_windows)
        self.main_button.pack(pady=50)

    def start_creating_windows(self):
        threading.Thread(target=self.create_multiple_windows).start()

    def create_multiple_windows(self):
        #while True:
        for index in range(10):
            self.create_new_window()
            time.sleep(0.01)

    def create_new_window(self):
        new_window = tk.Toplevel(self.root)
        new_window.title("Window")

        new_window.resizable(0, 0)
        new_window.overrideredirect(True)

        window_width = 256
        window_height = 144
        new_window.geometry(f"{window_width}x{window_height}")

        random_x_position = random.randint(0, self.root.winfo_screenwidth() - window_width)
        random_y_position = random.randint(0, self.root.winfo_screenheight() - window_height)

        new_window.geometry(f"{window_width}x{window_height}+{random_x_position}+{random_y_position}")

        random_colour = generate_random_colour()
        new_window.configure(bg=random_colour)

root = tk.Tk()
app = App(root)
root.mainloop()
