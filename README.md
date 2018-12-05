# 101_Object_Classification 
VGG-NET implemented in Tensorflow

The dataset used in this experiment is Caltech 101, you can find it at the following address:
http://www.vision.caltech.edu/Image_Datasets/Caltech101/

Credits:
L. Fei-Fei, R. Fergus and P. Perona. Learning generative visual models
from few training examples: an incremental Bayesian approach tested on
101 object categories. IEEE. CVPR 2004, Workshop on Generative-Model
Based Vision. 2004

Packages Requirements:
- Tensorflow
- TfLearn 
- Scipy
- Numpy

1) Data Preparation

-> Clone 101_Object_Classification repo
-> Download the dataset from Caltech Website
-> Extract dataset in working forlder 

-> Use "resizeme.py" python script to automatically resize and rename images for NN training. 70% of the dataset is used for training and 30% for validation. The dataset is automatically splitted using the script "resizeme.py"

The samples are now organized regarding the following structure:
Train/SUBFOLDER_0/CLASS0_IMG1.jpg
Train/SUBFOLDER_0/CLASS0_IMG2.jpg
...
Validate/SUBFOLDER_101/CLASS101_IMG15.jpg

2) Training

-> Launch train.py
-> Use "tensorboard --logdir=logs" to monitor training in your favorite browser

3) Testing

-> Launch predict.py
-> Monitor accuracy regarding unknown examples



