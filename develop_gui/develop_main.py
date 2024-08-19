import tkinter as tk
from testA import HomeScreen as Home
from testB import ScribbleScreen as Scri
from testC import LoadScreen as Load
from testD import CompleteScreen as Comp

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("2D to 3D Application")
        self.geometry("600x600")

        self.screen1 = Home(self, self.show_ScribbleScreen, self.show_LoadScreen)
        self.screen2 = Scri(self, self.show_HomeScreen)
        self.screen3 = Load(self, self.show_CompleteScreen)
        self.screen4 = Comp(self, self.show_HomeScreen)

        self.show_HomeScreen()

    def show_HomeScreen(self):
        self.screen1.pack(fill=tk.BOTH, expand=True)
        self.screen2.pack_forget()
        self.screen3.pack_forget()
        self.screen4.pack_forget()

    def show_ScribbleScreen(self):
        self.screen1.pack_forget()
        self.screen2.pack(fill=tk.BOTH, expand=True)
        self.screen3.pack_forget()
        self.screen4.pack_forget()

    def show_LoadScreen(self):
        self.screen1.pack_forget()
        self.screen2.pack_forget()
        self.screen3.pack(fill=tk.BOTH, expand=True)
        self.screen4.pack_forget()

        self.screen3.start_long_running_task()

    def show_CompleteScreen(self):
        self.screen1.pack_forget()
        self.screen2.pack_forget()
        self.screen3.pack_forget()
        self.screen4.pack(fill=tk.BOTH, expand=True)
    
    """
    def show_other_screen(self):
        self.screen1.pack_forget()
        self.screen2.pack_forget()
        self.screen3.pack(fill=tk.BOTH, expand=True)
    """

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
