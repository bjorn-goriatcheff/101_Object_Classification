from scipy import misc
import os

height = 400
width = 400

# resize images inside subfolders
def resize_img(path_img):
        im = misc.imread(path_img, mode="RGB")
        im = misc.imresize(im, (100, 100, 3))
        misc.imsave(path_img, im)

# Preprocess the dataset and resize the images
def preproc():
    # Dataset target
    path = '/home/bjo/Work/BJO/KINo-NN/101_ObjectCategories'
    nn_path = '/home/bjo/Work/BJO/KINo-NN'
    # List folders
    repertory = os.listdir(path)
    # Count folders
    categories = len(repertory)
    # Paths to train/validate
    train_path = os.path.join(nn_path, "train")
    val_path = os.path.join(nn_path, "validate")
    # Create subfolders train/validate
    os.mkdir(train_path)
    os.mkdir(val_path)
    # Create subfolders for categories
    for i in range(categories):
        # Subfolder name
        sub_name = "SUBFOLDER_" + str(i)
        # Paths to subfolders 
        train_sub_path = os.path.join(train_path, sub_name)    
        val_sub_path = os.path.join(val_path, sub_name)    
        # Create specific subfolder
        os.mkdir(train_sub_path)    
        os.mkdir(val_sub_path)
        # Repertory path
        rep_path = os.path.join(path, repertory[i])
        num_img = 0
        num_img_val = 0

        max_img = len(os.listdir(rep_path))
        max_tr = (max_img*7)/10
        for image in os.listdir(rep_path):
            # Image path
            img_path = os.path.join(rep_path, image)
            # Copy 70% of dataset to train set
            if(num_img  <  max_tr):
                tar_path = os.path.join(train_sub_path, "CLASS"+str(i)+"_IMG"+str(num_img)+".jpg")
                os.rename(img_path, tar_path)
                resize_img(tar_path)
                num_img += 1
            # Copy 30% of dataset to validate set
            else:
                tar_path = os.path.join(val_sub_path, "CLASS"+str(i)+"_IMG"+str(num_img_val)+".jpg")
                os.rename(img_path, tar_path)
                resize_img(tar_path)
                num_img_val += 1 

preproc()

