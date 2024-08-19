from PIL import ImageGrab
import tkinter

window = tkinter.Tk()
image_saved = False

# 書いた絵を保存
def capture():
        x = window.winfo_rootx()
        y = window.winfo_rooty()
        width = 600
        height = 400
        x_margin1 = 40
        y_margin1 = 40
        x_margin2 = 100
        y_margin2 = 100

        image = ImageGrab.grab(bbox=(x + x_margin1, y + y_margin1, x + width + x_margin2, y + height + y_margin2))
        image.save("data/screenshot.png")
        image_saved = True
        window.destroy()

class Scribble:

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

    def click1(self,event):
        self.canvas.create_oval(self.sx-20,self.sy-20,self.sx+20,self.sy+20,
                            fill = self.color.get(),
                            width = self.width.get())

    def click2(self,event):
        self.canvas.create_oval(self.sx-40,self.sy-30,self.sx+40,self.sy+30,
                           fill = self.color.get(),
                           width = self.width.get())



    def create_window(self):
        window.title("2D to 3D")
        self.canvas = tkinter.Canvas(window, bg = "black", 
                                 width = 600, height = 400)                             
        self.canvas.pack()
        quit_button = tkinter.Button(window, text = "終了",
                                 command = window.quit)
        quit_button.pack(side = tkinter.RIGHT)

        self.canvas.bind("<ButtonPress-1>", self.on_pressed)
        self.canvas.bind("<B1-Motion>", self.on_dragged)
        self.canvas.bind("<ButtonPress-2>",self.click1)
        self.canvas.bind("<ButtonPress-3>",self.click2)

        button = tkinter.Button(window, text="画面キャプチャ", command=capture)
        button.pack(padx=10, pady=10)



        COLORS = ["red", "white", "blue", "pink", "green","black"]
        self.color = tkinter.StringVar()                    
        self.color.set(COLORS[1])                             
        b = tkinter.OptionMenu(window, self.color, *COLORS) 
        b.pack(side = tkinter.LEFT)


        self.width = tkinter.Scale(window, from_ = 1, to = 10,
                               orient = tkinter.HORIZONTAL) 
        self.width.set(5)                                       
        self.width.pack(side = tkinter.LEFT)

        return window;

    def __init__(self):
        self.window = self.create_window();  
    
    def run(self):
        self.window.mainloop()


