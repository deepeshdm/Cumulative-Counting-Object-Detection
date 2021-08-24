## Cumulative Counting Object_Detecting using Tensorflow Object Detection


#### Here we use Object tracking & Cumulative counting to detect how many total boxes are taken inside the manufacturing tunnel by the workers,below is an example output of a video stream.The output can be generated from a video file or it can also be used for real-time surveillance in camera systems.


![](/EXAMPLES/example_gif.gif)


## Instructions for setup :
1] Create a new Python environment & install all packages mentioned in the requirements.txt file

2] Install the Tensorflow object detection API on your system.This is a bit tedious task and may cause errors,please refer to the below links :

https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/

https://youtu.be/dZh_ps8gKgs

3] Download the trained model (saved_model folder) from the below link :

https://drive.google.com/drive/folders/1AICgCnkSAtvTDh8DiX9yaDpslGqbIUsX?usp=sharing

## How to use :

The 'mainAPI.py' file is the main file & acts as an simple API.It imports the run_inference() function from another script,this function takes multiple parameters like file paths , detection threshold,skip_frames etc all of them are mentioned in detail inside the script.

#### NOTE : The model has been trained on images of fixed resolution (640x640),so the model wont function properly if given a video/image beyond that resolution.Recommended resolution for the input is (960x720).

### Detecting & Counting Objects inside Video file : 
The run_inference() method takes a video file path parameter,you just have to pass the location of your video file & the script will output another processed video. You can see an example output video inside the Examples folder.

### Detecting & Counting Objects from webcam : 
The run_inference() method takes a video file path parameter,if you dont provide a video file path then the script will use the webcam and also display the real time output on the screen. Make sure to adjust the 'skip_frames' parameter accordingly if the 'show_video'=True to get a smooth display of the output on the screen.

NOTE : The model has an approx accuracy of 90% which can be easily increased if further trained on good quality of image data.

Reference : https://github.com/TannerGilbert/Tensorflow-2-Object-Counting 
