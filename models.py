import sqlite3
from sqlite3 import Error

class TodosProjects:
    def __init__(self, db_file):
      self.conn = None
      try:
        self.conn = sqlite3.connect(db_file, check_same_thread=False)
        self.cur = self.conn.cursor()
      except sqlite3.Error as e:
        print(e)

    def create_project(self, project):
        sql ='''INSERT INTO projects(name, start_date, end_date)
             VALUES(?,?,?)'''

        self.cur.execute(sql, project)
        self.conn.commit()
        return self.cur.lastrowid

    def all_projects(self):
      self.cur.execute(f'SELECT * FROM projects')
      return self.cur.fetchall()
    
    def get_project(self, id):
      self.cur.execute(f"SELECT * FROM projects WHERE id = {id}")
      return self.cur.fetchone()

    def update(self, id, data):
        sql = f''' UPDATE projects
                SET name = ?, start_date = ?, end_date = ?
                WHERE id = {id}'''
        try:
            self.cur.execute(sql, data) 
            self.conn.commit()
            print("OK")
        except sqlite3.OperationalError as e:
            print(e)
    
db_file = "todos_base.db" # ale najpierw trzeba ją stworzyć funkcją w kodzie lub ręcznie w programie z bazami danych edit: stworzona
projects = TodosProjects(db_file)