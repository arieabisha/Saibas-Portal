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
def load_students():
  with engine.connect() as conn:
    result = conn.execute(text("select id, stdid, fname, mname, lname, date_format(dob, '%d/%m/%Y') as dob, notes, sex, concat(fname,' ', mname,' ',lname) as name  from student order by name"))
    return result.all()

def load_students_from_db():
  with engine.connect() as conn:
    query = text("select id, stdid, fname, mname, lname, date_format(dob, '%d/%m/%Y') as dob, date_format(dob, '%Y-%m-%d') as dob2, notes, sex, concat(fname,' ', mname,' ',lname) as name  from student order by name")
  
    result = conn.execute(query)
  
    students = []
    for row in result.all():
      students.append(row)
      
    return students

def add_student_to_db(data):
  with engine.connect() as conn:
    query = text(f"INSERT INTO student (stdid, fname, mname, lname, sex, dob, notes) VALUES ('{data['stdid']}', '{data['fname']}', '{data['mname']}', '{data['lname']}', '{data['sex']}', '{data['dob']}','{data['notes']}')")

  conn.close()
  conn = engine.connect()
  conn.execute(query)
  conn.commit()
   # conn.execute(query, {fname:data['fname'],mname: data['mname'],lname:data['lname'],sex:data['sex'],dob:data['dob']})
  #return query

def update_student_to_db(data):
  with engine.connect() as conn:
    query = text(f"UPDATE student SET stdid='{data['stdid']}', fname='{data['fname']}', mname='{data['mname']}', lname='{data['lname']}', sex='{data['sex']}', dob='{data['dob2']}', notes='{data['notes']}' WHERE id={data['id']}")
    
  conn.close()
  conn = engine.connect()
  conn.execute(query)
  conn.commit()


def delete_student_from_db(data):
  with engine.connect() as conn:
    query = text(f"DELETE FROM student WHERE id={data['id']}")

  conn.close()
  conn = engine.connect()
  conn.execute(query)
  conn.commit()
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
    
    


