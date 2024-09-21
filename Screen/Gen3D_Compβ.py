import tkinter as tk

class CompleteScreen(tk.Frame):
    def __init__(self, master, switch_screen):
        super().__init__(master, bg="#2B2B2B")
        self.switch_screen = switch_screen
        self.create_widgets()

    def create_widgets(self):
        """
        label = tk.Label(self, text="Load Complete!", font=("Helvetica", 24))
        label.pack(pady=20)

        button = tk.Button(self, text="Go to Home", command=self.switch_screen)
        button.pack(pady=20)
        """

        # タイトルラベル
        title_label = tk.Label(self, text="3D化完了！", font=("Helvetica", 32), fg="white", bg="#2B2B2B")
        title_label.pack(pady=20)

        # カスタムボタンの作成
        return_button = tk.Button(
            self, text="↶", command=self.switch_screen,
            font=("Helvetica", 24), bg="#FF6F61", fg="white",
            width=5, height=2, relief="flat", cursor="hand2", bd=0
        )
        return_button.pack(pady=10)

        # サブテキストラベル
        sub_text = tk.Label(self, text="ホームへ戻る", font=("Helvetica", 14), fg="#CCCCCC", bg="#2B2B2B")
        sub_text.pack(pady=10)
