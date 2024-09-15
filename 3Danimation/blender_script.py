
import bpy

# �����̃I�u�W�F�N�g���폜
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# OBJ�t�@�C����ǂݍ���
bpy.ops.import_scene.obj(filepath='3D_Data/mesh.obj')

# �J�����̐ݒ�
bpy.ops.object.camera_add(location=(0, -10, 5))
camera = bpy.context.active_object
bpy.context.scene.camera = camera

# �����_�����O�ݒ�
bpy.context.scene.render.image_settings.file_format = 'PNG'
bpy.context.scene.render.filepath = 'rendered_image.png'

# �摜�������_�����O
bpy.ops.render.render(write_still=True)
