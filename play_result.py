from ultralytics import YOLO
import cv2
# load yolov8 model
model = YOLO('final_korean_cam.pt')
# load video
video_path = '2.mp4'
cap = cv2.VideoCapture(video_path)
ret = True
# read frames
while ret:
    ret, frame = cap.read()
    if ret:
        # detect objects
        # track objects
        results = model.track(frame, persist=True)
        # plot results
        # cv2.rectangle
        # cv2.putText
        frame_ = results[0].plot()
        #print(results[0])
        # visualize
        cv2.imshow('frame', frame_)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break