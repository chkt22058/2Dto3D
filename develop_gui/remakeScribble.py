from PIL import ImageGrab
import tkinter

image_saved = False

class Scribble:
    def __init__(self):
        self.window = self.create_window();  

    def on_pressed(self, event):
        self.sx = event.x
        self.sy = event.y
        self.canvas.create_oval(self.sx, self.sy, event.x, event.y,
                                outline = self.color.get(),
                                width = self.width.get())

    def on_dragged(self, event):
        self.canvas.create_line(self.sx, self.sy, event.x, event.y,
                            fill = self.color.get(),
                            width = self.width.get())
        self.sx = event.x
        self.sy = event.y

    def create_window(self):
        window = tkinter.Tk()
        window.title("2D to 3D")
        self.canvas = tkinter.Canvas(window, bg = "black", 
                                 width = 600, height = 400)                             
        self.canvas.pack()
        quit_button = tkinter.Button(window, text = "終了",
                                 command = window.quit)
        quit_button.pack(side = tkinter.RIGHT)

        self.canvas.bind("<ButtonPress-1>", self.on_pressed)
        self.canvas.bind("<B1-Motion>", self.on_dragged)
        
        button = tkinter.Button(window, text="画面キャプチャ", command=self.capture)
        button.pack(padx=10, pady=10)

        COLORS = ["red", "white", "blue", "pink", "green","black"]
        self.color = tkinter.StringVar()                    
        self.color.set(COLORS[1])                             
        b = tkinter.OptionMenu(window, self.color, *COLORS) 
        b.pack(side = tkinter.LEFT)

        self.width = tkinter.Scale(window, from_ = 1, to = 10, orient = tkinter.HORIZONTAL) 
        self.width.set(5)                                       
        self.width.pack(side = tkinter.LEFT)

        return window
    
    def capture(self):
        x = self.window.winfo_rootx()
        y = self.window.winfo_rooty()
        width = 600
        height = 400
        x_margin1 = 40
        y_margin1 = 40
        x_margin2 = 100
        y_margin2 = 100

        image = ImageGrab.grab(bbox=(x + x_margin1, y + y_margin1, x + width + x_margin2, y + height + y_margin2))
        image.save("data/screenshot.png")
        image_saved = True
        self.window.destroy()
    
    def run(self):
        self.window.mainloop()

"""
if __name__ == "__main__":
    Scribble().run()
"""
