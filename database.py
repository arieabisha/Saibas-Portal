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
    result = conn.execute(text("select id, studentid, studentfname, studentmname, studentlname, date_format(studentdob, '%d/%m/%Y') as studentdob, notes, studentsex, concat(studentfname,' ', studentmname,' ',studentlname) as studentname  from student order by studentname"))
    return result.all()

def load_students_from_db():
  with engine.connect() as conn:
    query = text("select id, studentid, studentfname, studentmname, studentlname, date_format(studentdob, '%d/%m/%Y') as studentdob, date_format(studentdob, '%Y-%m-%d') as studentdob2, notes, studentsex, concat(studentfname,' ', studentmname,' ',studentlname) as studentname from student where isactive='Y' order by studentname")
  
    result = conn.execute(query)
  
    students = []
    for row in result.all():
      students.append(row)
      
    return students

def add_student_to_db(data):
  with engine.connect() as conn:
    query = text(f"INSERT INTO student (studentid, studentfname, studentmname, studentlname, studentsex, studentdob, notes, isactive, createdon) VALUES ('{data['stdid']}', '{data['fname']}', '{data['mname']}', '{data['lname']}', '{data['sex']}', '{data['dob']}','{data['notes']}', 'Y', now())")

  conn.close()
  conn = engine.connect()
  conn.execute(query)
  conn.commit()
   # conn.execute(query, {fname:data['fname'],mname: data['mname'],lname:data['lname'],sex:data['sex'],dob:data['dob']})
  #return query

def update_student_to_db(data):
  with engine.connect() as conn:
    query = text(f"UPDATE student SET studentid='{data['stdid']}', studentfname='{data['fname']}', studentmname='{data['mname']}', studentlname='{data['lname']}', studentsex='{data['sex']}', studentdob='{data['dob2']}', notes='{data['notes']}' WHERE id={data['id']}")
    
  conn.close()
  conn = engine.connect()
  conn.execute(query)
  conn.commit()


def delete_student_from_db(data):
  with engine.connect() as conn:
    #query = text(f"DELETE FROM student WHERE id={data['id']}")
    query = text(f"UPDATE student SET isactive='N' WHERE id={data['id']}")

  conn.close()
  conn = engine.connect()
  conn.execute(query)
  conn.commit()
  #return query

#master table

def load_menu_from_db():
  with engine.connect() as conn:
    query = text("select distinct menuid1, menuid2, menutitle, menupy, menupage from menu order by menuid1, menuid2")
    #query = text("select * from menu where menuid2=0 order by menuid1")
    result = conn.execute(query)
    menu = []
    for row in result.all():
      menu.append(row)

    return menu

def load_active_menu_from_db(menupy):
  with engine.connect() as conn:
    query = text("select menupage from menu where menupy = :val")
    #query = text("select * from menu where menuid2=0 order by menuid1")
    result = conn.execute(query,{"val": menupy})
    menupage = []
    for row in result.all():
      menupage.append(row)

    menupageremovelist = menupage[0]
    menupageremovetuple = menupageremovelist[0]
    menupage = menupageremovetuple
    
    return menupage

def load_submenum_from_db(data):
  with engine.connect() as conn:
    query = text(f"select * from menu where menuid1={data['menuid1']} order by menuid2")
    result = conn.execute(query)
    submenu = []
    for row in result.all():
      submenu.append(row)

    return submenu


def load_gender_from_db():
  with engine.connect() as conn:
    query = text("select id, sex, isactive from gender where isactive='Y' order by sex")

    result = conn.execute(query)
    gender = []
    for row in result.all():
      gender.append(row)

    return gender
    
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
    
    


