import sys
sys.path.append("/home/casezma/gltk/src/recognition/")
sys.path.append("/home/casezma/gltk/src/face_manager")
import cv2 as cv
import face_recognition as fr
from datetime import datetime
import face_queue as q

import recognition as recognition
capture = cv.VideoCapture(0)

face_descriptions = []
areas = []
known_faces_locations = []
while True:
    ret, frame = capture.read()
    cv.imshow("frame",frame)
    if cv.waitKey(1) == ord('q'):
       break
    elif cv.waitKey(1) == ord('s'):
        locations = fr.face_locations(frame)
        count = 0
        larger_area_index = []
        for (top,right,bottom,left) in locations:
            area = abs((top - bottom) * (right - left))
            areas.append(area)
            count += 1
        count = 0
        for area in areas:
            if area == max(areas) and len(locations) >=0 and count < len(locations):
                known_faces_locations.append(locations[count]) 
                data = {"timestamp":datetime.now(),"encoding":fr.face_encodings(frame,known_faces_locations)}
                q.put(**data)
                count +=1
        recognition.get_distance()
capture.release()
cv.destroyAllWindows()
