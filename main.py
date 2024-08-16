from lib import Cvt3dMod as cvt
from lib import Rigging as rig
from IPython.display import display
import ipywidgets as widgets

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
    # 各ボタンがクリックされたときの動作
def on_button1_click(b):
    print("ボタン1がクリックされました！")

def on_button2_click(b):
    print("ボタン2がクリックされました！")

def on_button3_click(b):
    print("ボタン3がクリックされました！")

# ボタン1を作成
button1 = widgets.Button(
    description="入力開始",
    tooltip='ボタン1をクリック',
    button_style='primary'
)
button1.on_click(on_button1_click)

# ボタン2を作成
button2 = widgets.Button(
    description="入力完了",
    tooltip='ボタン2をクリック',
    button_style='success'
)
button2.on_click(on_button2_click)

# ボタン3を作成
button3 = widgets.Button(
    description="戻る",
    tooltip='ボタン3をクリック',
    button_style='danger'
)
button3.on_click(on_button3_click)

# ボタンを横並びに配置するためのボックスを作成
box = widgets.HBox([button1, button2, button3])

# ボタンを表示
display(box)




