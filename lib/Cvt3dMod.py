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


