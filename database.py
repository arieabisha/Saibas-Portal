from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['db_connection_string'] 
engine = create_engine (
  db_connection_string,
  connect_args={
    "ssl": {
    "ssl_ca": "/etc/ssl/cert.pem"
    }
  })

# student
def load_student_cursor():
  with engine.connect() as conn:
    cursor=conn._cursor_execute(text("SELECT * FROM student"))
    return cursor.fetchall()


def load_students_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select id, stdid, fname, mname, lname, dob, notes, sex, concat(fname,' ', mname,' ',lname) as name  from student"))
  
    students = []
    for row in result.fetchall():
      students.append(row)
      return students

def add_student_to_db(data):
  with engine.connect() as conn:
    query = text(f"INSERT INTO student (fname, mname, lname, sex, dob, notes) VALUES ('{data['fname']}', '{data['mname']}', '{data['lname']}', '{data['sex']}', '{data['dob']}','')")

  conn.close()
  conn = engine.connect()
  conn.execute(query)
  conn.commit()
   # conn.execute(query, {fname:data['fname'],mname: data['mname'],lname:data['lname'],sex:data['sex'],dob:data['dob']})
  #return query
    
#job
def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
    #  jobs.append(dict(row))
      jobs.append(row)
    return jobs

def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("select *, format(salary,2) as sal2 from jobs where id = :val"), {"val": id})    
  job = []
  for row in result.all():
    job.append(row)
  return job
    
    


