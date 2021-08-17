# Cumulative Counting Object_Detecting using Tensorflow Object Detection

## Instructions for setup :
1] Create a new Python environment & install all packages mentioned in the requirements.txt file

2] Install the Tensorflow object detection API on your system.This is a bit tedious task and may cause errors,please refer to the below links :

https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/

https://youtu.be/dZh_ps8gKgs

## How to use :

The 'mainAPI.py' file is the main file & acts as an simple API.It imports the run_inference() function from another script,this function takes multiple parameters like file paths , detection threshold,skip_frames etc all of them are mentioned in detail inside the script.

The model has been trained to detect objects inside images of particular format,so if you give a video/image of another format the model may not produce any results.

<html>
  <head>
  </head>
  <body>
   <p float="left">
  <img src="/Display_Images/image1.jpeg" width="220" height="420" />
  <img src="/Display_Images/image2.jpeg" width="220" height="420" />
</p>
  </body>
  </html>



