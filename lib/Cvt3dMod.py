import os
import glob
import sys
import cv2
import argparse
import numpy as np
import matplotlib.pyplot as plt

import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision import transforms
from PIL import Image
import rembg


import subprocess

def run_a_py_with_args(args):
    command = ["python", "A.py"] + args
    result = subprocess.run(command, capture_output=True, text=True)
    



#dreamgaussian--------------------------------------

def preprocess(raw_path, args = []) :
    command = ["python", "./dreamgaussian/process.py"] + raw_path + args
    result = subprocess.run(command, capture_output=True, text=True)
    if(result.returncode != 0) :
        print("Standard Error:")
        print(result.stderr)

def training_gaussian(processed_path, args = ["--config configs/image.yaml"]) :
    command = ["python", "./dreamgaussian/main.py"] + args + ["input="] + processed_path
    result = subprocess.run(command, capture_output=True, text=True)
    if(result.returncode != 0) :
        print("Standard Error:")
        print(result.stderr)

def training_mesh(processed_path, args = ["--config configs/image.yaml"]) :
    command = ["python", "./dreamgaussian/main2.py"] + args + ["input="] + processed_path
    result = subprocess.run(command, capture_output=True, text=True)
    if(result.returncode != 0) :
        print("Standard Error:")
        print(result.stderr)
'''
def gen_obj(args) :
    command = ["python", "./dreamgaussian/process.py"] + args
    result = subprocess.run(command, capture_output=True, text=True)
    if(result.returncode != 0) :
        print("Standard Error:")                                                                                                                                                                                       
        print(result.stderr)
'''

#bpy-----------------
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
