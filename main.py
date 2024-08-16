# from lib import Cvt3dMod as cvt
# from lib import Rigging as rig
from lib import DrawPicture as draw
from PIL import Image 

if __name__ == "__main__":
    # 2D画像の取得(dataファイルにscreenshot.pngを保存)
    draw.Scribble().run()

    """
    # 2D画像を3D画像に変換
    image_2d = "data/screenshot.png"
    cvt.preprocess(image_2d)
    cvt.training_gaussian("data/image_2d_rgba.png")
    #cvt.training_mesh("data/image_2d_rgba.png")

    # 3D画像にリギング
    image_3d = "data/image_2d.obg"
    rig.main(image_3d)
    image_3d.save("data/image_3d.png")
    
    """




