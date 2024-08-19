import tkinter as tk

class HomeScreen(tk.Frame):
    def __init__(self, master, switch_screen1, switch_screen2):
        super().__init__(master)
        self.switch_screen1 = switch_screen1
        self.switch_screen2 = switch_screen2
        self.create_widgets()
    
    def create_widgets(self):
        label = tk.Label(self, text="Challenge 2D to 3D", font=("Helvetica", 24))
        label.pack(pady=20)
        
        button_a = tk.Button(self, text="Go to make illustration", command=self.switch_screen1, font=("Helvetica", 24))
        button_a.pack(pady=30)

        button_b = tk.Button(self, text="Go to make 3D", command=self.switch_screen2, font=("Helvetica", 24))
        button_b.pack(pady=30)

        button_c = tk.Button(self, text="Go to make Animation", font=("Helvetica", 24))
        button_c.pack(pady=30)

        quit_button = tk.Button(self, text="Exit", command=self.quit, font=("Helvetica", 10))
        quit_button.pack(side=tk.RIGHT, pady=10)

