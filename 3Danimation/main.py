import os
import subprocess
import tkinter as tk
from PIL import Image, ImageTk

# Blenderスクリプトを実行して画像を生成する関数
def render_obj_with_blender(obj_filepath, output_image_path):
    blender_script = f"""
import bpy

# 既存のオブジェクトを削除
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# OBJファイルを読み込み
bpy.ops.import_scene.obj(filepath='{obj_filepath}')

# カメラの設定
bpy.ops.object.camera_add(location=(0, -10, 5))
camera = bpy.context.active_object
bpy.context.scene.camera = camera

# レンダリング設定
bpy.context.scene.render.image_settings.file_format = 'PNG'
bpy.context.scene.render.filepath = '{output_image_path}'

# 画像をレンダリング
bpy.ops.render.render(write_still=True)
"""
    
    # Blenderをサブプロセスでヘッドレスモード実行
    with open('blender_script.py', 'w') as script_file:
        script_file.write(blender_script)
    
    subprocess.run([r'C:/Program Files/Blender Foundation/Blender 4.2/blender.exe', '--background', '--python', 'blender_script.py'])


# 画像をTkinterのLabelに表示する関数
def update_image(label, image_path):
    img = Image.open(image_path)
    img = img.resize((400, 400), Image.ANTIALIAS)  # サイズ調整
    img_tk = ImageTk.PhotoImage(img)
    label.config(image=img_tk)
    label.image = img_tk

# GUIを構築する関数
def create_gui(obj_filepath):
    output_image_path = 'rendered_image.png'
    
    # 最初のレンダリング
    render_obj_with_blender(obj_filepath, output_image_path)
    
    # Tkinterウィンドウのセットアップ
    root = tk.Tk()
    root.title("3D Object Preview")
    
    # 初期画像の表示
    label = tk.Label(root)
    label.pack(pady=20)
    update_image(label, output_image_path)
    
    # 視点を変更して再レンダリングするためのボタン
    def on_rotate():
        # ここで新しい視点に変更してレンダリング
        render_obj_with_blender(obj_filepath, output_image_path)
        update_image(label, output_image_path)

    rotate_button = tk.Button(root, text="Rotate View", command=on_rotate)
    rotate_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    obj_filepath = "3D_Data/mesh.obj"  # OBJファイルのパスを指定
    create_gui(obj_filepath)