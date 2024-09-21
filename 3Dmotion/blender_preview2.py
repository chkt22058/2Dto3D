import bpy
import sys
import os

def generate_preview(obj_path, output_path, x_rot, y_rot, z_rot):
    print("Starting generate_preview function")
    
    bpy.ops.wm.read_factory_settings(use_empty=True)
    print(f"Importing OBJ file: {obj_path}")
    
    try:
        bpy.ops.import_scene.obj(filepath=obj_path)
    except Exception as e:
        print(f"Error importing OBJ file: {e}")
        return

    print("Getting imported object")
    if bpy.context.selected_objects:
        obj = bpy.context.selected_objects[0]
    else:
        print("No objects were imported")
        return

    print("Positioning object")
    bpy.ops.object.select_all(action='DESELECT')
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='BOUNDS')
    obj.location = (0, 0, 0)
    
    obj.rotation_euler = (x_rot * (3.14159 / 180), y_rot * (3.14159 / 180), z_rot * (3.14159 / 180))  # ラジアンに変換

    print("Adding camera")
    bpy.ops.object.camera_add(location=(0, -5, 0))
    camera = bpy.context.active_object
    camera.rotation_euler = (1.5708, 0, 0)  # 90度のX軸回転
    
    bpy.context.scene.camera = camera
    
    print("Adding light")
    bpy.ops.object.light_add(type='SUN', location=(5, -5, 5))
    
    print("Setting up render")
    bpy.context.scene.render.engine = 'CYCLES'
    bpy.context.scene.render.film_transparent = True
    bpy.context.scene.render.resolution_x = 800
    bpy.context.scene.render.resolution_y = 600
    
    print(f"Rendering to: {output_path}")
    bpy.context.scene.render.filepath = output_path
    try:
        bpy.ops.render.render(write_still=True)
    except Exception as e:
        print(f"Error during rendering: {e}")
        return

    print(f"Preview generated. Saved to: {output_path}")

if __name__ == "__main__":
    print("Script started")
    obj_path = sys.argv[-4]  # OBJファイルのパス
    output_path = sys.argv[-3]  # 出力パス
    x_rotation = float(sys.argv[-2])  # X軸回転
    y_rotation = float(sys.argv[-1])  # Y軸回転
    z_rotation = float(sys.argv[-1])  # Z軸回転

    print(f"Input OBJ path: {obj_path}")
    print(f"Output preview path: {output_path}")
    generate_preview(obj_path, output_path, x_rotation, y_rotation, z_rotation)
    print("Script finished")
