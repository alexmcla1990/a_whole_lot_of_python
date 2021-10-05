from imageai.Detection import VideoObjectDetection
import os
import cv2

curDir = os.getcwd()

camera = cv2.Videocapture

detector = VideoObjectDetection()
detector.setModelTypeAsTinyYOLOv3()
detector.setModelPath(os.path.join(curDir, "yolo.h5"))
detector.loadModel()

video_path = detector.detectObjectsFromVideo(camera_input=camera,
                                output_file_path=os.path.join(curDir, "cam1")
                                , frames_per_second=4, log_progress=True)

print(video_path)