# Cumulative Counting Object_Detecting using Tensorflow Object Detection

![](/Examples/example_gif.gif)

## Instructions for setup :
1] Create a new Python environment & install all packages mentioned in the requirements.txt file

2] Install the Tensorflow object detection API on your system.This is a bit tedious task and may cause errors,please refer to the below links :

https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/

https://youtu.be/dZh_ps8gKgs

## How to use :

The 'mainAPI.py' file is the main file & acts as an simple API.It imports the run_inference() function from another script,this function takes multiple parameters like file paths , detection threshold,skip_frames etc all of them are mentioned in detail inside the script.

#### NOTE : The model has been trained to detect objects inside images of particular format,so if you give a video/image of another format the model may not produce any results.Below the image on the left display the correct format while the image on the right display the incorrect format.

<html>
  <head>
  </head>
  <body>
   <p float="left">
  <img src="/Examples/correct format.jpg" width="250" height="250" />
  <img src="/Examples/wrong format.jpg" width="250" height="250" />
</p>
  </body>
  </html>


### Detecting & Counting Objects inside Video file : 
The run_inference() method takes a video file path parameter,you just have to pass the location of your video file & the script will output another processed video. You can see an example output video inside the Examples folder.

### Detecting & Counting Objects from webcam : 
The run_inference() method takes a video file path parameter,if you dont provide a video file path then the script will use the webcam and also display the real time output on the screen. Make sure to adjust the 'skip_frames' parameter accordingly if the 'show_video'=True to get a smooth display of the output on the screen.

NOTE : The model has an approx accuracy of 70% which can be easily increased if further trained on good quality of image data.
