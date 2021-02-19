#ml libraries
import tensorflow as tf
from tensorflow import keras
#user files
import images.preprocessing as preprocess


def cnn():
    #create cnn
    cnn = create_cnn()
    #load data
    preprocess.load_images()


def create_cnn(layers=3, kernel=3, filters=3, activation_function='leaky_relu'):
    cnn = keras.Sequential()
    cnn.add(keras.layers.Conv2D(filters, kernel, activation=activation_function, input_shape=(28,28)))
    cnn.add(keras.layers.Conv2D())
    



