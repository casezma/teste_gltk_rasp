import sys
sys.path.append("/home/casezma/gltk/src/data")
from data import Data
import face_recognition as fr

image = fr.load_image_file("images/maia.jpg")
locations = fr.face_locations(image)
encoding = fr.face_encodings(image,locations)[0]
data = Data()
string = ""
for item in encoding:
    string += ","  + item.__str__()
string.replace("\n","")
data.insert_face("maia",string)

