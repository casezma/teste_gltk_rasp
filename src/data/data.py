import sqlite3


class Data:

    def __init__(self):
        self.connection = sqlite3.connect("../data/faces_registration.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS faces (id INTEGER PRIMARY KEY AUTOINCREMENT, name text, encoding text)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS log (id INTEGER PRIMARY KEY AUTOINCREMENT,id_faces INTEGER,timestamp text, status INTEGER)")

    def insert_face(self,name,encoding,id_face):
        self.cursor.execute("INSERT INTO faces(name,encoding) VALUES (?,?)",(name,encoding))
        self.connection.commit()
        self.cursor.close()
        self.connection.close()
        print("Face "+ name + " incluida")

    def insert_log(self, id_faces,timestamp):
        self.cursor.execute("INSERT INTO log(id_faces,timestamp,status) VALUES (?,?,1)",(id_faces,timestamp))
        self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def select_faces(self):
        self.cursor.execute("SELECT name, encoding, id FROM faces")
        fetch = self.cursor.fetchall()
        raw_encodings = fetch[0][1]
        name = fetch[0][0]
        values = []
        for register in fetch:
            raw_encodings = register[1].split(",")
            string = ""
            index_value = 0
            encoding = []
            for item in raw_encodings:
                if item != '':
                    string =  str(item)
                    index_value = float(string)
                    encoding.append(index_value)
            values.append({"name":register[0],"encoding":encoding,"id":register[2]})
        return values
        
        
