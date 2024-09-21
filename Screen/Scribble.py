import tkinter as tk
from PIL import ImageGrab, Image, ImageOps

class ScribbleScreen(tk.Frame):
    def __init__(self, master, switch_screen):
        super().__init__(master)
        self.switch_screen = switch_screen
        self.create_widgets()

    def create_widgets(self):
        # キャンバス画面ウィジェット作成
        self.canvas = tk.Canvas(self, bg="white", width=600, height=400)
        # self.canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.canvas.grid(row=0, column=0, columnspan=4, sticky="nsew")

        # キャプチャ画面ウィジェット作成
        capture_button = tk.Button(self, text="画面キャプチャ", command=self.capture_canvas)
        # capture_button.pack(side=tk.BOTTOM, pady=10)
        capture_button.grid(row=2, column=0, padx=10, pady=10)

        # 筆色の変更ウィジェット作成
        COLORS = ["red", "white", "blue", "pink", "green", "black"]
        self.color = tk.StringVar()
        self.color.set(COLORS[5])
        color_menu = tk.OptionMenu(self, self.color, *COLORS)
        # color_menu.pack(side=tk.LEFT, padx=10)
        color_menu.grid(row=1, column=0, padx=10)

        # 消しゴムウィジェット作成
        eraser_button = tk.Button(self, text="Eraser", command=self.use_eraser)
        # eraser_button.pack(side=tk.LEFT, padx=10)
        eraser_button.grid(row=1, column=1, padx=10)

        # 筆線のウィジェット作成
        self.width = tk.Scale(self, from_=1, to=10, orient=tk.HORIZONTAL)
        self.width.set(5)
        # self.width.pack(side=tk.LEFT, padx=10)
        self.width.grid(row=1, column=2, padx=10)

        # 終了ウィジェット作成
        quit_button = tk.Button(self, text="Exit", command=self.switch_screen)
        # quit_button.pack(side=tk.BOTTOM, pady=10)
        quit_button.grid(row=2, column=2, padx=10, pady=10)

        # マウスによる描画
        self.canvas.bind("<ButtonPress-1>", self.on_pressed)
        self.canvas.bind("<B1-Motion>", self.on_dragged)

        # リセットボタン作成
        reset_button = tk.Button(self, text="リセット", command=self.reset_canvas)
        # reset_button.pack(side=tk.BOTTOM, padx=20, pady=20)
        reset_button.grid(row=2, column=1, padx=10, pady=10)

    # 消しゴムを使用する関数
    def use_eraser(self):
        self.color.set("white")

    def on_pressed(self, event):
        self.sx = event.x
        self.sy = event.y
        self.canvas.create_oval(self.sx, self.sy, event.x, event.y,
                                outline=self.color.get(),
                                width=self.width.get())
    def on_dragged(self, event):
        self.canvas.create_line(self.sx, self.sy, event.x, event.y,
                                fill=self.color.get(),
                                width=self.width.get())
        self.sx = event.x
        self.sy = event.y
    
    """
    # 画面の保存
    def capture(self):
        self.update_idletasks()

        x = self.winfo_rootx()
        y = self.winfo_rooty()
        width = self.winfo_width()
        height = self.winfo_height()
        
        x_margin1 = 40
        y_margin1 = 40
        x_margin2 = 100
        y_margin2 = 100

        image = ImageGrab.grab(bbox=(x + x_margin1, y + y_margin1, x + width + x_margin2, y + height + y_margin2))
        image.save("./2D_data/screenshot.png")

        
        #image.show()
    
    """

    def reset_canvas(self):
        self.canvas.delete("all")  # キャンバス上のすべてのアイテムを削除
        self.canvas.configure(bg="white")  # 背景色を白に設定
    
    # キャンバス画面のみキャプチャ
    def capture_canvas(self):
        self.canvas.postscript(file="2D_data/temp_canvas.ps", colormode='color')
        image = Image.open("2D_data/temp_canvas.ps")
        image = ImageOps.expand(image, border=0, fill='white')
        image.save("./2D_data/screenshot.png")