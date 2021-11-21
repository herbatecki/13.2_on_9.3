# ex_02_create_tables.py

import sqlite3
from sqlite3 import Error

db_file = "virtual_flask/tasks/task_13.2_on_9.3/13.2_on_9.3/projects.db"

def create_connection(db_file):
   """ create a database connection to the SQLite database
       specified by db_file
   :param db_file: database file
   :return: Connection object or None
   """
   conn = None
   try:
       conn = sqlite3.connect(db_file)
       return conn
   except Error as e:
       print(e)

   return conn

def execute_sql(conn, sql):
   """ Execute sql
   :param conn: Connection object
   :param sql: a SQL script
   :return:
   """
   try:
       c = conn.cursor()
       c.execute(sql)
   except Error as e:
       print(e)

if __name__ == "__main__":

   create_projects_sql = """
   -- projects table
   CREATE TABLE IF NOT EXISTS projects (
      id integer PRIMARY KEY,
      name text NOT NULL,
      start_date text,
      end_date text
   );
   """

   create_tasks_sql = """
   -- tasks table
   CREATE TABLE IF NOT EXISTS tasks (
      id integer PRIMARY KEY,
      project_id integer NOT NULL,
      name VARCHAR(250) NOT NULL,
      description TEXT,
      status VARCHAR(15) NOT NULL,
      start_date text NOT NULL,
      end_date text NOT NULL,
      FOREIGN KEY (project_id) REFERENCES projects (id)
   );
   """

   conn = create_connection(db_file)
   if conn is not None:
       execute_sql(conn, create_projects_sql)
       execute_sql(conn, create_tasks_sql)
       conn.close()
