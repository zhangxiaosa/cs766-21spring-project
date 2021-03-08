import models
import data

myModel = models.OriginCNN()

myData = data.Cifar10()

myModel.build()

myModel.train(myData.train_images, myData.train_labels, myData.test_images, myData.test_labels, 1)

myModel.evaluate(myData.test_images, myData.test_labels)