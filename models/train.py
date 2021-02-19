import images.preprocessing as imgs
import pandas as pd
from tkinter import filedialog
import platform
import tkinter

'''
    load images / preprocess / load dqn / load carView / load cnn
'''


class trained_network():
    def __init__(self, data=None):
        self.data = data
        self.driving_log = None
        self.model_input = []


    def set_model_input(self):
        if platform.system() == 'Windows':
            #select file
            root = tkinter.Tk()
            filename = tkinter.filedialog.askopenfile(parent=root, mode='rb', title='Choose driving log')

        self.driving_log = pd.read_csv(filename)
        ncols = len(self.driving_log.columns)
        for row in self.driving_log.iterrows():
            print("row", row)
            self.model_input.append([row[1][0], row[1][1], row[1][2], row[1][3], row[1][4], row[1][5]])

        print(self.model_input[0])

    #network to drive on street 
    def drive_network(self):
        print("***%%% training driving network %%%%***")
        #load images
        images_directory = imgs.load_images()
        #reshape images
        self.data = imgs.reshape(images_directory)


    #detect obstacles(cnn)
    def obstacle_network(self):
        pass


    #avoid collision
    def safety_network(self):
        pass