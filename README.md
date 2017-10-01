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
