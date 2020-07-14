import sys
sys.path.append('/home/casezma/gltk/src/data')
sys.path.append('/home/casezma/gltk/src/face_manager')
import face_recognition as fr
from data import Data
import face_queue as queue
import numpy as np

def get_distance():        
    if queue.isEmpty() != True:
        data = Data()
        name = "Unknown"
        query = data.select_faces()
        known_face_encodings = []
        for register in query:
           known_face_encodings.append(register["encoding"])
        queue_register = queue.get()
        queue_face = queue_register["encoding"]
        face_distances = fr.face_distance(known_face_encodings, queue_face[0])
        best_match_index = np.argmin(face_distances)
        if face_distances[best_match_index]:
            name = query[best_match_index]["name"]
            print(name)
            data.insert_log(query[best_match_index]["id"],queue_register["timestamp"])
            return name
        else:
            return ""
