import tkinter as tk
from tkinter import messagebox
import threading
import time

class LoadScreen(tk.Frame):
    def __init__(self, master, switch_screen):
        super().__init__(master)
        self.switch_screen = switch_screen
        self.create_widgets()
    
    def create_widgets(self):
        
        label = tk.Button(self, text="Exit", command=self.quit)
        label.pack(side=tk.RIGHT, pady=10)
        
        button = tk.Button(self, text="Go to Home", command=self.switch_screen)
        button.pack(pady=10)

        # 背景色を設定
        self.configure(bg='#282C34')

        # ラベルを作成してウィンドウに追加
        label = tk.Label(self, text="Loading, please wait...", fg='#FFFFFF', bg='#282C34', font=('Helvetica', 16))
        label.pack(pady=50)

        # プログレスバーのようなエフェクトを追加
        progress = tk.Canvas(self, width=300, height=20, bg='#3C3F41')
        progress.pack(pady=20)
        progress_bar = progress.create_rectangle(0, 0, 0, 20, fill="#61AFEF")
        def animate():
            current_width = progress.coords(progress_bar)[2]
            if current_width < 300:
                progress.coords(progress_bar, 0, 0, current_width + 75, 20)
                self.after(100, animate)
            else:
                progress.coords(progress_bar, 0, 0, 0, 20)  # リセット
                self.after(100, animate)
        animate()

    def start_long_running_task(self):
        self.after(5000, self.complete_task) 

    def complete_task(self):
        self.switch_screen()
        
