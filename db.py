import sqlite3

class Database:
    def __init__(self,db):
        self.con=sqlite3.connect(db)
        self.cur=self.con.cursor()
        sql=""" CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY,
        name TEXT,
        age TEXT,
        gender TEXT,
        doa TEXT,
        sno TEXT,
        pno TEXT,
        address TEXT,
        quota TEXT
        )"""
        self.cur.execute(sql)
        self.con.commit()
        sql=""" CREATE TABLE IF NOT EXISTS sem(
        id INTEGER,
        sem1 TEXT DEFAULT '0',
        sem2 TEXT DEFAULT '0',
        sem3 TEXT DEFAULT '0',
        sem4 TEXT DEFAULT '0',
        sem5 TEXT DEFAULT '0',
        sem6 TEXT DEFAULT '0',
        sem7 TEXT DEFAULT '0',
        sem8 TEXT DEFAULT '0'
        
        )"""
        self.cur.execute(sql)
        self.con.commit()
    def insert(self,name,age,gender,doa,sno,pno,address,quota):
        self.cur.execute("""INSERT INTO students VALUES(NULL,?,?,?,?,?,?,?,?)
""",(name,age,gender,doa,sno,pno,address,quota))
        self.con.commit()
    def insert1(self,id,sem1,sem2,sem3,sem4,sem5,sem6,sem7,sem8):
        self.cur.execute("""INSERT INTO sem VALUES(?,?,?,?,?,?,?,?,?)
""",(id,sem1,sem2,sem3,sem4,sem5,sem6,sem7,sem8))
        self.con.commit()
    def fetch(self):
        self.cur.execute("SELECT * FROM students")
        rows=self.cur.fetchall()
        return rows
    def fetch1(self):
        self.cur.execute("SELECT * FROM sem")
        rows=self.cur.fetchall()       
        return rows
    def remove(self,id):
        self.cur.execute("DELETE FROM students WHERE id=?",(id,))
        self.con.commit()
    def remove1(self,id):
        self.cur.execute("DELETE FROM sem WHERE id=?",(id,))
        self.con.commit()
    def update(self,id,name,age,gender,doa,sno,pno,address,quota):
        self.cur.execute("""UPDATE students SET name=?,age=?,gender=?,doa=?,sno=?,pno=?,address=?,quota=? WHERE id=? """,(name,age,gender,doa,sno,pno,address,quota,id))
        self.con.commit()
    def update1(self,id,sem1,sem2,sem3,sem4,sem5,sem6,sem7,sem8):
        self.cur.execute("""UPDATE sem SET sem1=?,sem2=?,sem3=?,sem4=?,sem5=?,sem6=?,sem7=?,sem8=? WHERE id=? """,(sem1,sem2,sem3,sem4,sem5,sem6,sem7,sem8,id))
        self.con.commit()
    def search(self,key):
        self.cur.execute("SELECT * FROM students where name like ? or age like ? or gender like ? or doa like ? or sno like ? or pno like ? or address like ? or quota like ? or id like ?",(key,key,key,key,key,key,key,key,key))
        rows=self.cur.fetchall()


        return rows
        

