# VinBigdata Vietnamese Face Aging

## Introduction
This repository is based on the ["High Resolution Face Age Editing"](https://arxiv.org/pdf/2005.04410v1.pdf) paper and original repository [HRFAE](https://github.com/InterDigitalInc/HRFAE). The goal of the model is to take an input image with any age and produce an output image with a specified age. Due to resource constraints, we could only train the model on 128x128 resolution images instead of the 1024x1024 resolution mentioned in the paper. During experimentation, we discovered that the model architecture was better suited for high-resolution images, and when trained on 128x128 images, it performed poorly.

We then considered two options:

- Directly modifying the model architecture to better suit low-quality images.
- Using pre-trained weights from the 1024x1024 image training and continuing training with 128x128 images.

In this repository, we have directly modified the model architecture to better suit low-quality images.

![](images/arch.png)

## Train model
### Dataset
We trained the model on [FFHQ dataset](https://github.com/NVlabs/ffhq-dataset).
We have built the functionality of this repository on Kaggle. To run the model, first, you need to download the original Caffe model and convert it to PyTorch format. We use the converter called "caffemodel2pytorch," which was released by Vadim Kantorov. Then, name the PyTorch model as "dex_imdb_wiki.caffemodel.pt" and upload it to the dataset in the Kaggle notebook you are using.  

Afterward, you just need to run the following lines of code one by one to complete the training process. You can find the GitHub link attached for forking and customizing the code (https://github.com/Edge-Zerox/VinBigData_Project_Hrfaefork).  
Run the following code to train with config '001':

    !git clone -b Hopee https://github.com/Edge-Zerox/Hrfae-fork.git
    cd /kaggle/working/Hrfae-fork

    !pip install --upgrade tensorflow
    !pip install PyYAML Pillow tensorboardX torchvision tensorboard_logger
    !python /kaggle/working/Hrfae-fork/train.py --config 001

    

## Inference
To perform inference with the model, follow these steps:
1. Place the images you want to infer from into the "test/input" directory.

2. Run the following shell script commands.
    ```bash
        cd src/
        python test.py
    ```
3. The output images are saved in the "test/output" directory


