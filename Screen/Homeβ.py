import tkinter as tk

class HomeScreen(tk.Frame):
    def __init__(self, master, switch_screen1, switch_screen2, switch_screen3):
        super().__init__(master)
        self.switch_screen1 = switch_screen1
        self.switch_screen2 = switch_screen2
        self.switch_screen3 = switch_screen3
        self.create_widgets()
    
    def create_widgets(self):
        # タイトルラベル
        title_label = tk.Label(self, text="Challenge 2D to 3D", font=("Helvetica", 24), fg="#4A90E2")
        title_label.pack(pady=20)

        btn_font = ("Helvetica", 16)  # ボタンのフォントサイズ

        # ボタンのスタイルと作成
        btn_illustration = tk.Button(self, text="Go to make illustration", command=self.switch_screen1, bg="#7ED321", fg="white", font=btn_font)
        btn_3d = tk.Button(self, text="Go to make 3D", command=self.switch_screen2, bg="#F5A623", fg="white", font=btn_font)
        btn_animation = tk.Button(self, text="Go to make Animation", command=self.switch_screen3, bg="#9013FE", fg="white", font=btn_font)
        btn_exit = tk.Button(self, text="Exit", command=self.quit, bg="#D0021B", fg="white", font=btn_font)

        # ボタンの配置
        btn_illustration.pack(expand=True, fill='both', padx=20, pady=10)
        btn_3d.pack(expand=True, fill='both', padx=20, pady=10)
        btn_animation.pack(expand=True, fill='both', padx=20, pady=10)
        btn_exit.pack(expand=True, fill='both', padx=20, pady=10)

