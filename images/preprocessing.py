from tkinter import filedialog
import platform
import tkinter
import torch
import numpy as np
import os
from PIL import Image


#load images
def load_images(directory=None, read_mode=None):
    if platform.system() == 'Windows':
        #select file
        root = tkinter.Tk()
        if read_mode == None:
            directory = tkinter.filedialog.askdirectory()
        else:
            directory = tkinter.filedialog.askdirectory(parent=root, mode=read_mode, title='Choose a directory')

        if directory != None:
            print("directory ", directory)
            return directory


#return images to greyscale
def grayscale(image):
    pass


#reshape images to dimension
def reshape(directory, dim=(28,28, 1)):
    print("dir ", directory)
    reshaped_data = {}
    #iterate through images
    for file in os.listdir(directory):
        if not file.endswith(".ini"):
            img = Image.open(directory + "/" + file)
            npdata = np.asarray(img)
            #save it as tensor
            img = torch.from_numpy(npdata)
            #add to dictionary
            reshaped_data["IMG/" + file] = img

    return reshaped_data
    

def testing():
    pass

