
import bpy

# 既存のオブジェクトを削除
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# OBJファイルを読み込み
bpy.ops.import_scene.obj(filepath='3D_Data/mesh.obj')

# カメラの設定
bpy.ops.object.camera_add(location=(0, -10, 5))
camera = bpy.context.active_object
bpy.context.scene.camera = camera

# レンダリング設定
bpy.context.scene.render.image_settings.file_format = 'PNG'
bpy.context.scene.render.filepath = 'rendered_image.png'

# 画像をレンダリング
bpy.ops.render.render(write_still=True)
