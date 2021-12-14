# Cumulative Counting and Object Tracking 

### OBJECTIVE

The main goal of this project is to create a object detection system which can optimally track the movement of objects and also perform cumulative counting of objects. This application is supposed to be used in a industrial factory where workers manually move manufacturing goods into the production tunnel,this application will take input from the factory's 'surveillance camera system' and track how many containers were taken inside and outside the production tunnel by workers in real-time.

<div align="center">
  <h4> (Example output videos from the surveillance camera system)</h4>
</div>

<div align="center">
<Img src="/EXAMPLES/example_gif.gif">
<Img src="/EXAMPLES/result2_gif.gif">
</div>
  
## Data Collection & Labelling  

For training this model we would need bunch of images with their ground-truth co-ordinates. The Images were collected by extracting optimal image frames from hours of surveillance camera videos.
  
In total 2000 were collected which were later manually annotated using the Image labelling tool called "LabelImg",which you can find [here](https://github.com/tzutalin/labelImg).


## Instructions for setup
1. Git clone the repository on your local system
```
git clone https://github.com/deepeshdm/Cumulative-Counting-Object-Detection.git
```
  
2. Create a new Python environment & install all packages mentioned in the requirements.txt file
  
```
pip install - r requirements.txt
```

2. Install the Tensorflow object detection API on your system.This is a bit tedious task and may cause errors,please refer to the below links :
  - https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/
  - https://youtu.be/dZh_ps8gKgs
 
4. Download the trained model (saved_model folder) by clicking [here](https://drive.google.com/drive/folders/1AICgCnkSAtvTDh8DiX9yaDpslGqbIUsX?usp=sharing).


## API Guide :

The 'mainAPI.py' file is the main file & acts as an simple API.It imports the run_inference() function from another script,this function takes multiple parameters like file paths , detection threshold,skip_frames etc all of them are mentioned in detail inside the script.

#### NOTE : The model has been trained on images of fixed resolution (640x640),so the model wont function properly if given a video/image beyond that resolution.Recommended resolution for the input is (960x720).
  
-------------------------------------------------------------------------

#### Detecting and Counting Objects inside Video file :
The run_inference() method takes a video file path parameter,you just have to pass the location of your video file & the script will output another processed video. You can see an example output video inside the Examples folder.

#### Detecting and Counting Objects from webcam :
The run_inference() method takes a video file path parameter,if you dont provide a video file path then the script will use the webcam and also display the real time output on the screen. Make sure to adjust the 'skip_frames' parameter accordingly if the 'show_video'=True to get a smooth display of the output on the screen.

#### NOTE : The model has an approx accuracy of 90% which can be easily increased if further trained on good quality of image data.

-------------------------------------------------------------------------

References : https://github.com/TannerGilbert/Tensorflow-2-Object-Counting 
