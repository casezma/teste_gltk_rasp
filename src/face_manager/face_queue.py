from queue import Queue

q = Queue()
face_description = []

def put(**kwargs):
    timestamp = kwargs['timestamp']
    encoding = kwargs['encoding']
    q.put({"timestamp":timestamp,"encoding":encoding})        

def get():
    return q.get()

def isEmpty():
    return q.empty()