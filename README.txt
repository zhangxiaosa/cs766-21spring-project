
README FILE


Functions/Notebooks:

ParseData
Author: Nick Chelales

Since dataset is large, training batches are created each with approximately 20% of the entire data. Each batch contains a distribution of classes proportional to the overall dataset. Training batches are stored as .npy files and can be accessed by running np.load with allow_pickle = True. Before creating batches, samples are randomly shuffled twice. 

Since each image is varying size, they are stored in a list. They can be accessed in the following manner:

#load the data
XtrainBatch = np.load('Xtrain_Batch0.npy', allow_pickle = True)
YtrainBatchLabel = np.load('Ytrain_Batch0.npy', allow_pickle = True)


#access a particular image, for example, number 5
ImageIndex = 5
Image5 = XtrainBatch[ImageIndex]
Image5Label = YtrainBatch[ImageIndex]

Note that the Label information is also stored in a list, an each element is a 2x1 vector with the patient name (e.g. 'Number_right') as the first element and class label as the second element.

A test batch is also created, in the same manner as the training batch.

CAUTION-IMPORTANT: Because of the way the batches are created, the data in each batch is sorted by class (i.e. first 5000 or so values of each batch are class 0, then class 1 etc). It is recommended to shuffle the dataset once importing prior to performing training. 


CreateEvenSets

This script works similiar to ParseData, but creates evenly distributed datasets. 


PerformSVM

This script works by performing kernel based SVM on the given dataset (change path to perform on different dataset). The script performs 5-fold cross validation to determine the most optimal hyperparameters for kernel based SVM. In addition, it generates a classification report and confusion matrix for the given results. 
