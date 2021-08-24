
"""
AUTHOR : Deepesh Mhatre
Date of writing : 16/8/2021
License : MIT LICENSE

Please read the README.md file which contains all the necessary details.

"""


# ---------------------------------------------------------------

import cv2,warnings
from object_detection.utils import label_map_util
from tensorflow_cumulative_object_counting \
    import run_inference, load_model

warnings.filterwarnings('ignore')

# ---------------------------------------------------------------

# SET ALL THE NECESSARY PARAMETERS BELOW

# Path to saved_model foler downloaded from google drive
MODEL_PATH = r"C:\Users\dipesh\Desktop\Final Product\saved_model"

# NOTE : The model has been trained on images of fixed resolution (640x640),
# so the model wont function properly if given a video/image beyond that 
# resolution.cRecommended resolution for the input is (960x720).

# Path to your video file (if not given webcam will be used)
VIDEO_PATH = r"C:\Users\dipesh\Downloads\2021-08-06_01-16-01_utc_scanning-tunnel.mp4"

# Path to label_map file
LABEL_MAP_PATH = r"C:/Users/dipesh/Desktop/label_map.pbtxt"

# Path to save the output video with name of the video file (Use .mp4 extension).
# If None output won\'t be saved
SAVE_PATH = r"C:/Users/dipesh/Desktop/RESULT_VIDEO2.mp4"

# Detection threshold
THRESHOLD = 0.5

# Region of Interest (Roi) position
ROI = 0.6

# No. of frames to skip b/w using object detection model
SKIP_FRAMES = 20

# Shows the video frames during processing if True
# (set False if video longer than 3-5 mins)
SHOW_VIDEO = False

# Object to Track & Count,we can choose one of 2 classes,
# "Tunnel_Box" or "person"
OBJECT2COUNT = "Tunnel_Box"

# ---------------------------------------------------------------


if __name__ == "__main__":

    detection_model = load_model(MODEL_PATH)
    category_index = label_map_util.create_category_index_from_labelmap(
        LABEL_MAP_PATH, use_display_name=True)

    # open video file if path given or-else use the webcam
    if VIDEO_PATH != '':
        cap = cv2.VideoCapture(VIDEO_PATH)
    else:
        SHOW_VIDEO = True
        SKIP_FRAMES=50
        cap = cv2.VideoCapture(0)


    if not cap.isOpened():
        print("Error opening video stream or file")
        print("Try giving a video path")

    run_inference(detection_model, category_index, cap, labels=OBJECT2COUNT, threshold=THRESHOLD,
                  roi_position=ROI, x_axis=False, skip_frames=SKIP_FRAMES,
                  save_path=SAVE_PATH, show=SHOW_VIDEO)
