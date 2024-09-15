import bpy

# 既存のオブジェクトを削除
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# OBJファイルを読み込み
try:
    bpy.ops.import_scene.obj(filepath='C:/Users/torak/3D_Data/mesh.obj')
    print("OBJファイルのインポートに成功しました。")
except Exception as e:
    print("エラーが発生しました:", e)

# カメラの設定
bpy.ops.object.camera_add(location=(0, -10, 5))
camera = bpy.context.active_object
bpy.context.scene.camera = camera

# レンダリング設定
bpy.context.scene.render.image_settings.file_format = 'PNG'
bpy.context.scene.render.filepath = 'C:/Users/torak/3D_Data/rendered_image.png'

# 画像をレンダリング
bpy.ops.render.render(write_still=True)
