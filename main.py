from lib import Cvt3dMod as cvt
from lib import Rigging as rig

def main(): 

    # 2D→3D 
    image_2d = "lib/dreamgaussian-main/data/test.png"
    cvt.preprocess(image_2d)
    cvt.training_gaussian("data/image_2d_rgba.png")
    #cvt.training_mesh("data/image_2d_rgba.png")


    # 3D→3Dリギング
    image_3d = "data/image_2d.obg"
    rig.main(image_3d)

    print()
    

if __name__ == "__main__":
    main()