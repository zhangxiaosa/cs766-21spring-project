import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt

# reference: https://www.tensorflow.org/tutorials/images/cnn

class OriginCNN(object):
  """docstring for OriginCNN"""
  def __init__(self):
    self.optimizer = 'adam'
    self.loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
    # will add more properties


  def build(self):
    model = models.Sequential()
    model.add(layers.Conv2D(32, (3, 3), strides=(3,3), activation='relu', input_shape=(1000, 1000)))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(32, (3, 3), strides=(3,3), activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(32, (3, 3), strides=(3,3), activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))

    model.add(layers.Flatten())
    model.add(layers.Dense(32, activation='relu'))
    model.add(layers.Dense(2))

    model.summary()
    model.compile(optimizer=self.optimizer,
                loss=self.loss,
                metrics=['accuracy'])
    self.model = model

  def build_cifar(self):
    model = models.Sequential()
    model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))

    model.add(layers.Flatten())
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(10))

    model.summary()
    model.compile(optimizer=self.optimizer,
                loss=self.loss,
                metrics=['accuracy'])
    self.model = model


  def train(self, train_images, train_labels, test_images, test_labels, epochs):
    self.history = self.model.fit(train_images, train_labels, epochs=epochs, 
        validation_data=(test_images, test_labels))


  def evaluate(self, test_images, test_labels):
    plt.plot(self.history.history['accuracy'], label='accuracy')
    plt.plot(self.history.history['val_accuracy'], label = 'val_accuracy')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.ylim([0.5, 1])
    plt.legend(loc='lower right')

    test_loss, test_acc = self.model.evaluate(test_images, test_labels, verbose=2)

    print(test_acc)

# class ResNet(object):
#   def __init__(self):
#     # do similiar thing
    
