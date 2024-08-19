import tkinter as tk

class CompleteScreen(tk.Frame):
    def __init__(self, master, switch_screen):
        super().__init__(master, bg="lightgreen")
        self.switch_screen = switch_screen
        self.create_widgets()

    def create_widgets(self):
        label = tk.Label(self, text="Load Complete!", font=("Helvetica", 24))
        label.pack(pady=20)

        button = tk.Button(self, text="Go to Home", command=self.switch_screen)
        button.pack(pady=20)
