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
        root.forget()  # ロード画面を閉じる 
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
    # ラベルを作成してウィンドウに追加
    label = tk.Label(root, text="Loading, please wait...", padx=20, pady=20)
    label.pack()
    
    # ウィンドウのサイズと位置を設定
    root.geometry("300x100+500+300")
    

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
