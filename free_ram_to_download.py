import tkinter as tk
import time
import threading
import random

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Window")
        self.root.geometry("480x320")
        self.main_button = tk.Button(self.root, text="Create Windows", command=self.start_creating_windows)
        self.main_button.pack(pady=50)

    def start_creating_windows(self):
        threading.Thread(target=self.create_error_windows).start()

    def create_error_windows(self):
        while True:
            self.create_window()
            time.sleep(0.01)

    def create_window(self):
        new_window = tk.Toplevel(self.root)
        new_window.title("Window")
        new_window.geometry("200x100")
        x = random.randint(0, self.root.winfo_screenwidth() - 200)
        y = random.randint(0, self.root.winfo_screenheight() - 100)
        new_window.geometry(f"200x100+{x}+{y}")

        label = tk.Label(new_window, text="Text")
        label.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
