import bpy
import sys
import os

def generate_preview(obj_path, output_path):
    # シーンをクリア
    bpy.ops.wm.read_factory_settings(use_empty=True)

    # OBJファイルのインポート
    bpy.ops.import_scene.obj(filepath=obj_path)
    
    # インポートされたオブジェクトを取得
    obj = bpy.context.selected_objects[0]
    
    # オブジェクトを原点に配置
    bpy.ops.object.select_all(action='DESELECT')
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='BOUNDS')
    obj.location = (0, 0, 0)
    
    # カメラを追加
    bpy.ops.object.camera_add(location=(0, -5, 0))
    camera = bpy.context.active_object
    camera.rotation_euler = (1.5708, 0, 0)  # 90度のX軸回転
    
    # カメラをアクティブに設定
    bpy.context.scene.camera = camera
    
    # ライトを追加
    bpy.ops.object.light_add(type='SUN', location=(5, -5, 5))
    
    # レンダリング設定
    bpy.context.scene.render.engine = 'CYCLES'
    bpy.context.scene.render.film_transparent = True
    bpy.context.scene.render.resolution_x = 800
    bpy.context.scene.render.resolution_y = 600
    
    # レンダリングを実行
    bpy.context.scene.render.filepath = output_path
    bpy.ops.render.render(write_still=True)

    print(f"Preview generated. Saved to: {output_path}")

if __name__ == "__main__":
    obj_path = sys.argv[-2]  # コマンドライン引数からOBJファイルのパスを取得
    output_path = sys.argv[-1]  # コマンドライン引数から出力パスを取得
    generate_preview(obj_path, output_path)
