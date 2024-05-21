from flask import Flask, redirect, render_template, json, request, url_for, flash, session
from sqlalchemy import DATE
from database import load_jobs_from_db, load_job_from_db, load_students_from_db, add_student_to_db, load_students, update_student_to_db, delete_student_from_db

app = Flask(__name__)
app.secret_key = 'super secret'

@app.route("/")
def hello_world():
  #jobs = load_jobs_from_db()
  students = load_students_from_db()
  return render_template('index.html',
                          students=students)

  #return render_template('home.html', 
  #                       jobs = jobs, 
  #                       company_name = 'Saibas')

#student route

@app.route("/students")
def list_students():
#  students = load_students_from_db()
  students = load_students()
  return json.dumps(students, default=str)

@app.route("/student/apply", methods=['post'])
def add_student():
  data = request.form
  
  query = add_student_to_db(data)
  
  flash("Murid berhasil ditambahkan")
  
  return redirect(url_for('hello_world'))

  #return json.dumps(query, default=str)

@app.route("/student/update", methods=['post'])
def update_student():
  data = request.form
  query = update_student_to_db(data)
  flash("Murid berhasil diupdate")
  return redirect(url_for('hello_world'))

@app.route("/student/delete", methods=['post'])
def delete_student():
  data = request.form
  query = delete_student_from_db(data)
  flash("Murid berhasil dihapus")
  return redirect(url_for('hello_world'))
  #return json.dumps(query, default=str)

#@app.route("/delete/<id>", methods = ['get','post'] )
#def delete(id):
#  my_data = Data.query.get(id)
#  db.session.delete(my_data)
#  db.session.commit()
#  flash("Data deleted")
#  return redirect(url_for('hello_world'))

#job route
@app.route("/jobs")
def list_jobs():
  jobs = load_jobs_from_db()
  #jobs = { 
  #    "Modules" : 15, 
  #   "Subject" : "Data Structures and Algorithms", 
  #} 
  return json.dumps(jobs,default=str)

@app.route("/job/<id>")
def show_job(id):
  job = load_job_from_db(id)
  #return json.dumps(job,default=str)
  if not job:
    return "Not Found", 404
    
  return render_template('jobpage.html', 
                         job=job)

if __name__ == '__main__' :
  app.run(host='0.0.0.0',debug=True)