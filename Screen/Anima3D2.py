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

        # 回転用スライダーの追加
        self.x_rotation = tk.DoubleVar(value=0)
        self.y_rotation = tk.DoubleVar(value=0)
        self.z_rotation = tk.DoubleVar(value=0)

        x_slider = tk.Scale(self, from_=0, to=360, orient=tk.HORIZONTAL, 
                            label="X Rotation", variable=self.x_rotation)
        y_slider = tk.Scale(self, from_=0, to=360, orient=tk.HORIZONTAL, 
                            label="Y Rotation", variable=self.y_rotation)
        z_slider = tk.Scale(self, from_=0, to=360, orient=tk.HORIZONTAL, 
                            label="Z Rotation", variable=self.z_rotation)

        # スライダーを配置
        x_slider.pack(pady=5)
        y_slider.pack(pady=5)
        z_slider.pack(pady=5)

        # プレビュー画像を表示するためのキャンバスを追加
        self.canvas = tk.Canvas(self, width=800, height=600)
        self.canvas.pack()

        self.obj_path = None
        
        # Blenderの実行ファイルのパスを正確に設定
        self.blender_path = r"C:/Program Files/Blender Foundation/Blender 3.6/blender.exe"

        # スクリプトのディレクトリを取得
        if getattr(sys, 'frozen', False):
            self.script_dir = sys._MEIPASS
        else:
            self.script_dir = os.path.dirname(os.path.abspath(__file__))

    def load_obj(self):
        self.obj_path = filedialog.askopenfilename(filetypes=[("OBJ files", "*.obj")])
        if self.obj_path:
            print(f"Loaded OBJ: {self.obj_path}")

    def auto_rig(self):
        if not self.obj_path:
            print("Please load an OBJ file first.")
            return

        blender_script = r"C:/Users/torak/Documents/App/2Dto3D/3Dmotion/blender_auto_rig.py"
        
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

        blender_script = r"C:/Users/torak/Documents/App/2Dto3D/3Dmotion/blender_preview2.py"
        preview_path = os.path.splitext(self.obj_path)[0] + "_preview.png"

        command = [
            self.blender_path,
            "--background",
            "--python", blender_script,
            "--",
            self.obj_path,
            preview_path,
            str(self.x_rotation.get()),
            str(self.y_rotation.get()),
            str(self.z_rotation.get())
        ]

        try:
            result = subprocess.run(command, check=True, capture_output=True, text=True)
            print("Preview generation output:")
            print(result.stdout)
            if result.stderr:
                print("Errors during preview generation:")
                print(result.stderr)
            
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
        image = Image.open(image_path)
        image = image.resize((800, 600), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        self.canvas.delete("all")
        self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        self.canvas.image = photo
