import tkinter as tk
from tkinter import messagebox
import threading
import time
import draw_paint_test as draw
def running_task():
    # バックグラウンドで実行する処理（例えば、ファイルのダウンロードや計算など）
    time.sleep(5)  # 5秒間待機（例として）
def check_task_complete():
    # タスクが完了したかをチェックし、完了していればメインウィンドウを表示
    if not background_task.is_alive():  # スレッドが生きているかを確認  （※2D→3D画像に加工されたかに変更する）
        root.destroy()  # ロード画面を閉じる
        draw.Scribble().run()  # メインウィンドウを表示　（※ロードが終わった後の画面表示）
    else:
        root.after(100, check_task_complete)  # 100ミリ秒後に再チェック
"""
ロード画面の作成
show_loading_screen()に，デザインの処理を施す
"""
def show_loading_screen():
    global root, background_task
    # ロード画面用のウィンドウを作成
    root = tk.Tk()
    """
    ここから下にコードを追加，変更してGUIのデザインをしてほしい
    """
    root.title("Loading...")
    # ウィンドウのサイズと位置を設定
    root.geometry("400x200+500+300")
    # 背景色を設定
    root.configure(bg='#282C34')
    # ラベルを作成してウィンドウに追加
    label = tk.Label(root, text="Loading, please wait...", fg='#FFFFFF', bg='#282C34', font=('Helvetica', 16))
    label.pack(pady=50)
    # プログレスバーのようなエフェクトを追加
    progress = tk.Canvas(root, width=300, height=20, bg='#3C3F41')
    progress.pack(pady=20)
    progress_bar = progress.create_rectangle(0, 0, 0, 20, fill="#61AFEF")
    def animate():
        current_width = progress.coords(progress_bar)[2]
        if current_width < 300:
            progress.coords(progress_bar, 0, 0, current_width + 15, 20)
            root.after(100, animate)
        else:
            progress.coords(progress_bar, 0, 0, 0, 20)  # リセット
            root.after(100, animate)
    animate()
    """
    これより下のコードはこのままで
    """
    # バックグラウンドスレッドで長時間処理を実行
    background_task = threading.Thread(target=running_task, daemon=True)
    background_task.start()
    # ロード画面を表示し続ける
    root.after(100, check_task_complete)
    # メインループを開始
    root.mainloop()
# ロード画面を表示
show_loading_screen()