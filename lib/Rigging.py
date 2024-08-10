import bpy

def import_model(filepath):
    bpy.ops.import_scene.obj(filepath=filepath)

def create_armature():
    bpy.ops.object.armature_add()

def auto_rig():
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.parent_set(type='ARMATURE_AUTO')

def save_file(filepath):
    bpy.ops.wm.save_as_mainfile(filepath=filepath)

def main():
    model_path = "path/to/your/model.obj"
    output_path = "path/to/save/your/rigged_model.blend"
    
    import_model(model_path)
    create_armature()
    auto_rig()
    save_file(output_path)

if __name__ == "__main__":
    main()
