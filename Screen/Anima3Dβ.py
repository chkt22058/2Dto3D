import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import subprocess
import os
import sys

class AnimaScreen(tk.Frame):
    def __init__(self, master, switch_screen):
        super().__init__(master, bg="#2B2B2B")
        self.switch_screen = switch_screen

        self.master = master
        master.title("3D Model Viewer and Auto-Rigger")

        # ボタンの作成
        button_width = 15
        button_height = 2
        
        btn_load_obj = tk.Button(self, text="Load OBJ", command=self.load_obj, 
                          bg="#FF6F61", fg="white", font=("Helvetica", 16), 
                          width=button_width, height=button_height)
        
        btn_auto_rig = tk.Button(self, text="Auto Rig", command=self.auto_rig, 
                          bg="#FF6F61", fg="white", font=("Helvetica", 16), 
                          width=button_width, height=button_height)
        
        btn_preview = tk.Button(self, text="Preview", command=self.preview, 
                         bg="#FF6F61", fg="white", font=("Helvetica", 16), 
                         width=button_width, height=button_height)
        
        btn_go_home = tk.Button(self, text="Go to Home", command=self.switch_screen, 
                         bg="#FF6F61", fg="white", font=("Helvetica", 16), 
                         width=button_width, height=button_height)
        
        # ボタンを配置
        btn_load_obj.pack(pady=10)
        btn_auto_rig.pack(pady=10)
        btn_preview.pack(pady=10)
        btn_go_home.pack(pady=10)

        """
        self.load_button = tk.Button(self, text="Load OBJ", command=self.load_obj)
        self.load_button.pack()

        self.auto_rig_button = tk.Button(self, text="Auto Rig", command=self.auto_rig)
        self.auto_rig_button.pack()

        self.preview_button = tk.Button(self, text="Preview", command=self.preview)
        self.preview_button.pack()

        self.button = tk.Button(self, text="Go to Home", command=self.switch_screen)
        self.button.pack()

        """
        # プレビュー画像を表示するためのキャンバスを追加
        self.canvas = tk.Canvas(self, width=800, height=600)
        self.canvas.pack()

        self.obj_path = None
        
        # Blenderの実行ファイルのパスを正確に設定
        self.blender_path = r"C:/Program Files/Blender Foundation/Blender 3.6/blender.exe"
        # 注意: パスはあなたのシステムの実際のBlenderインストール場所に合わせて変更してください

        # スクリプトのディレクトリを取得
        if getattr(sys, 'frozen', False):
            # PyInstallerで実行可能ファイルにパッケージ化された場合
            self.script_dir = sys._MEIPASS
        else:
            # 通常のPythonスクリプトとして実行された場合
            self.script_dir = os.path.dirname(os.path.abspath(__file__))

    def load_obj(self):
        self.obj_path = filedialog.askopenfilename(filetypes=[("OBJ files", "*.obj")])
        if self.obj_path:
            print(f"Loaded OBJ: {self.obj_path}")

    def auto_rig(self):
        if not self.obj_path:
            print("Please load an OBJ file first.")
            return

        # Blenderスクリプトのパスを取得
        # blender_script = os.path.join(self.script_dir, "./3Dmotion/blender_auto_rig.py")
        blender_script = r"C:/Users/torak/Documents/App/2Dto3D/3Dmotion/blender_auto_rig.py"

        # Blenderスクリプトを実行
        try:
            result = subprocess.run([self.blender_path, "--background", "--python", blender_script, "--", self.obj_path], 
                                    check=True, capture_output=True, text=True)
            print("Auto-rigging output:")
            print(result.stdout)
            if result.stderr:
                print("Errors during auto-rigging:")
                print(result.stderr)
        except subprocess.CalledProcessError as e:
            print(f"Error during auto-rigging: {e}")
            print("Error output:")
            print(e.output)
        except FileNotFoundError:
            print(f"Blender executable not found at {self.blender_path}. Please check the path.")

    def preview(self):
        if not self.obj_path:
            print("Please load an OBJ file first.")
            return

        # Blenderスクリプトのパスを取得
        # blender_script = os.path.join(self.script_dir, "./3Dmotion/blender_preview.py")
        blender_script = r"C:/Users/torak/Documents/App/2Dto3D/3Dmotion/blender_preview.py"

        # プレビュー画像の出力パスを設定
        preview_path = os.path.splitext(self.obj_path)[0] + "_preview.png"

        # コマンドを構築
        command = [
            self.blender_path,
            "--background",
            "--python", blender_script,
            "--",
            self.obj_path,
            preview_path
        ]

        # Blenderでプレビューを生成
        try:
            result = subprocess.run(command, check=True, capture_output=True, text=True)
            print("Preview generation output:")
            print(result.stdout)
            if result.stderr:
                print("Errors during preview generation:")
                print(result.stderr)
            
            # プレビュー画像を表示
            self.display_preview(preview_path)
        except subprocess.CalledProcessError as e:
            print(f"Error during preview generation: {e}")
            print("Command output:")
            print(e.output)
            print("Command stderr:")
            print(e.stderr)
        except FileNotFoundError:
            print(f"Blender executable not found at {self.blender_path}. Please check the path.")        

    def display_preview(self, image_path):
        # 画像を読み込み
        image = Image.open(image_path)
        # キャンバスのサイズに合わせてリサイズ
        image = image.resize((800, 600), Image.LANCZOS)

        # PhotoImageオブジェクトを作成
        photo = ImageTk.PhotoImage(image)

        #--------------------------------------

        # キャンバスのサイズを取得
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()

        # キャンバスの中央に画像を配置する座標を計算
        x_offset = (canvas_width - image.width) // 2
        y_offset = (canvas_height - image.height) // 2

        #-----------------------------------------

        # キャンバスをクリア
        self.canvas.delete("all")  # これで以前の画像を削除

        # キャンバスに新しい画像を表示
        self.canvas.create_image(x_offset, y_offset, anchor=tk.NW, image=photo)

        # 参照を保持（ガベージコレクションを防ぐため）
        self.canvas.image = photo
