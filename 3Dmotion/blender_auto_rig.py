import bpy
import sys
import os

def auto_rig(obj_path):
    # OBJファイルのインポート
    bpy.ops.import_scene.obj(filepath=obj_path)
    
    # インポートされたオブジェクトを取得
    obj = bpy.context.selected_objects[0]
    
    # Rigifyのメタリグを追加
    bpy.ops.object.armature_human_metarig_add()
    metarig = bpy.context.active_object

    # メタリグをオブジェクトに合わせて調整
    metarig.scale = obj.dimensions
    metarig.location = obj.location

    # Rigifyを使用してリグを生成
    bpy.ops.pose.rigify_generate()

    # 生成されたリグを取得
    rig = bpy.context.active_object

    # オブジェクトをリグの子にする
    obj.parent = rig
    
    # 自動ウェイトペインティング
    bpy.ops.object.parent_set(type='ARMATURE_AUTO')

    # 結果を保存
    output_path = os.path.splitext(obj_path)[0] + "_rigged.blend"
    bpy.ops.wm.save_as_mainfile(filepath=output_path)

    print(f"Auto-rigging complete. Saved to: {output_path}")

if __name__ == "__main__":
    obj_path = sys.argv[-1]  # コマンドライン引数からOBJファイルのパスを取得
    auto_rig(obj_path)
