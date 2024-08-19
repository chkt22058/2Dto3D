import tkinter as tk
from testA import HomeScreen as home
from testB import ScribbleScreen as scri
from testC import LoadScreen as load

def show_screen1():
    screen1.pack(fill=tk.BOTH, expand=True)
    screen2.pack_forget()
    screen3.pack_forget()

def show_screen2():
    screen1.pack_forget()
    screen2.pack(fill=tk.BOTH, expand=True)
    screen3.pack_forget()

def show_screen3():
    screen1.pack_forget()
    screen2.pack_forget()
    screen3.pack(fill=tk.BOTH, expand=True)

root = tk.Tk()
root.title("2D to 3D")
root.geometry("600x500")

screen1 = home(root, show_screen2, show_screen3)
screen2 = scri(root, show_screen1)
screen3 = load(root, show_screen1)

if __name__ == "__main__":
    show_screen1()
    root.mainloop()
