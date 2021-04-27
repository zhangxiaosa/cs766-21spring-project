
README FILE

Information regarding this course project can be found on the project website: INSERT COURSE PROJECT WEBSITE HERE

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
Author: Nick Chelales

This script works similiar to ParseData, but creates evenly distributed datasets. 


PerformSVM
Author: Nick Chelales

This script works by performing kernel based SVM on the given dataset (change path to perform on different dataset). The script performs 5-fold cross validation to determine the most optimal hyperparameters for kernel based SVM. In addition, it generates a classification report and confusion matrix for the given results.


SVMResults Folder:

Each model iteration is associated with a particular timestamp, which matches the filenames of those files in the SVM Results folder. 
The following list associates each model with a timestamp:


3 Layered-CNN Models:

-20-04-2021 00:49:35
  -Dataset: Entire given dataset
  -Model Architecture: Preprocessing ---> 3 layered CNN ---> SVM
-16-04-2021 14:48:57
  -Dataset: Subsection of given data with even class distribution
  -Model Architecture: Preprocessing ---> 3 layered CNN ---> SVM
-16-04-2021 00:41:45
  -Dataset: Subsection of given data with even class distribution
  -Model Architecture: 3 layered CNN ---> SVM
-21-04-2021 15:09:26
  -Dataset: Dataset consisting of only classes 0 and 4
  -Model Architecture: Preprocessing --> 3 layered CNN ---> SVM
-09-04-2021 20:50:32
  -Dataset: Dataset consisting of only classes 0 and 4
  -Model Architecture: 3 layered CNN ---> SVM

Resnet CNN Models:

-22-04-2021 17:58:41
  -Dataset: Subsection of given data with even class distribution
  -Model Architecture: Preprocessing ---> Resnet ---> SVM
-20-04-2021 23:46:49
  -Dataset: Subsection of given data with even class distribution
  -Model Architecture: Resnet ---> SVM
-22-04-2021 14:43:41
  -Dataset: Dataset consisting of only classes 0 and 4
  -Model Architecture: Preprocessing -->  Resnet ---> SVM
-20-04-2021 17:43:17
  -Dataset: Dataset consisting of only classes 0 and 4
  -Model Architecture: Resnet ---> SVM











