
# coding: utf-8
# Reference:
# In[1]:

import urllib

def download_mnist(dataset="training"):

    DOWNLOAD_ROOT = "http://yann.lecun.com/exdb/mnist/"

    TRAIN_LABEL = "train-labels-idx1-ubyte.gz"
    TRAIN_IMAGE = "train-images-idx3-ubyte.gz"
    TEST_LABEL = "t10k-labels-idx1-ubyte.gz"
    TEST_IMAGE = "t10k-images-idx3-ubyte.gz"

    DATASET_PATH = "datasets/MNIST"
    if dataset == "training":
        label_url=os.path.join(DOWNLOAD_ROOT,TRAIN_LABEL)
        image_url=os.path.join(DOWNLOAD_ROOT,TRAIN_IMAGE)

        label_path=os.path.join(DATASET_PATH,TRAIN_LABEL)
        image_path=os.path.join(DATASET_PATH,TRAIN_IMAGE)
        urllib.request.urlretrieve(image_url,image_path)
        urllib.request.urlretrieve(label_url,label_path)
        load_file(label_path,image_path)

    if dataset == "testing":
        label_url=os.path.join(DOWNLOAD_ROOT,TEST_LABEL)
        image_url=os.path.join(DOWNLOAD_ROOT,TEST_IMAGE)

        label_path=os.path.join(DATASET_PATH,TEST_LABEL)
        image_path=os.path.join(DATASET_PATH,TEST_IMAGE)

        urllib.request.urlretrieve(image_url,image_path)
        urllib.request.urlretrieve(label_url,label_path)
        load_file(label_path,image_path)
    else:
        print("Dataset only can be 'testing' or 'training'")


# In[2]:
import gzip
import shutil
def load_file(label_path=".",image_path="."):

    img_data=image_path.replace(".gz","")
    label_data=label_path.replace(".gz","")
    if label_path == "."or image_path == ".":
        printf("Please input the file path")
    else:
        with gzip.open(label_path,'rb') as f_in:
            with open("datasets/MNIST/t10k-labels-idx1-ubyte",'wb') as f_out:
                f_content=f_in.read()
                f_out.write(f_content)
        with gzip.open(image_path,'rb') as f_in:
            with open("datasets/MNIST/t10k-images-idx3-ubyte",'wb') as f_out:
                    f_content=f_in.read()
                    f_out.write(f_content)
# In[3]:
import numpy as np
import os
import struct
def load_mnist(dataset="training", path="."):

    IMG_HEADSIZE=16
    LABEL_HEADSIZE=8
    if dataset == "training":
        fname_img = os.path.join(path, 'train-images-idx3-ubyte')
        fname_lbl = os.path.join(path, 'train-labels-idx1-ubyte')
    elif dataset == "testing":
        fname_img = os.path.join(path, 't10k-images-idx3-ubyte')
        fname_lbl = os.path.join(path, 't10k-labels-idx1-ubyte')
    else:
        raise ValueError("dataset must be 'testing' or 'training'")

    img=open(fname_img,"rb")
    label=open(fname_lbl,"rb")

    img_magic,img_num,img_rows,img_columns=struct.unpack(">IIII",img.read(IMG_HEADSIZE))
    img.seek(IMG_HEADSIZE,os.SEEK_SET)
    img_data=np.fromfile(img,dtype=np.uint8).reshape(img_num,img_rows*img_columns)
    label_magic,label_num=struct.unpack(">II",label.read(LABEL_HEADSIZE))
    label.seek(LABEL_HEADSIZE,os.SEEK_SET)
    label_data=np.fromfile(label,dtype=np.uint8)

    return img_data,label_data



# In[4]:
import matplotlib
import matplotlib.pyplot as plt

def showDigit(image_array=np.zeros((28,28),dtype=np.uint8)):
    image=image_array.reshape(28,28)
    plt.imshow(image,cmap=matplotlib.cm.binary,interpolation="nearest")
    plt.axis("off")
    plt.show()
