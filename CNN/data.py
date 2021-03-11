import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt

# https://www.tensorflow.org/tutorials/images/cnn

class Cifar10(object):
  """docstring for OriginCNN"""
  def __init__(self):
    # cifar10 is used for debugging
    (train_images, self.train_labels), (test_images, self.test_labels) = datasets.cifar10.load_data()

    # Normalize pixel values to be between 0 and 1
    self.train_images, self.test_images = train_images / 255.0, test_images / 255.0
    print(type(self.train_images))
    # exit()

# class DR(object):
#     def __init__(self):
#     # load DR dataset
#     self.train_images
