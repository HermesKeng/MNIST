# MNIST
> This fuction sets is refer to https://gist.github.com/akesling/5358964 to implement reading the MNIST dataset 

- Background: I'm the begin to learn Machine Learning through [Hands-On Machine Learning with Scikit-Learn and TensorFlow](http://shop.oreilly.com/product/0636920052289.do). There are some problems about example codes, when I start to learn  in Classification section (CH3). The original method in sklearn method can't download MNIST dataset, so I start to refer to other solution to write the program to download the dataset, and show the data in program.

- Descrition: There are four function in the MNIST.py, and I am goint t give you some introduction.
  - download_mnist: 
    Go to the [THE MNIST DATABASE](http://yann.lecun.com/exdb/mnist/) to download and decompress the dataset.
  - load_file:
    Load the file which have already downloaded and transform the gz file to binary file
  - load_mnist:
    Read the Binary file a and get the handwriting dataset and label
  - showDigit:
    Show the specified digit when you give the image in the dataset 

- Image Size: The image size is 28 * 28, so the total size of image is 784 pixel
- Train Set : 60000 images and label
- Test Set : 10000 images and label

- Details : In the [THE MNIST DATABASE](http://yann.lecun.com/exdb/mnist/) document, it tells us for each compress file is a binary file. We need to transform it to corresponding data type, and we can know the binary stroe format at the end of the document


** These code is my first try to decompress image, if there is any advice to my code, please give me some note , Thanks
