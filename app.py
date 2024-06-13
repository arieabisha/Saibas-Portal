from flask import Flask, redirect, render_template, json, request, url_for, flash, session, logging
from sqlalchemy import DATE
from wtforms import Form, StringField, TextAreaField, PasswordField, validators, SelectField
from passlib.hash import sha256_crypt
from database import load_jobs_from_db, load_job_from_db, load_students_from_db, add_student_to_db, load_students, update_student_to_db, delete_student_from_db, load_gender_from_db, load_menu_from_db, load_active_menu_from_db

app = Flask(__name__)
app.secret_key = 'super secret'

@app.route("/")
def hello_world():
  #jobs = load_jobs_from_db()
  menus = load_menu_from_db()
  #return json.dumps(gender, default=str)
  #gender = load_gender_from_db()
  #students = load_students_from_db()
  #return render_template('studentindex.html', 
  #                       students = students, 
  #                       gender = gender)

  return render_template('home.html', 
                         menus = menus, 
                         company_name = 'Saibas')

#student route

@app.route("/students")
def list_students():
#  students = load_students_from_db()
  students = load_students()
  return json.dumps(students, default=str)

@app.route("/student/index")
def index_student():

  menus = load_menu_from_db()
  gender = load_gender_from_db()
  students = load_students_from_db()
  menupage = load_active_menu_from_db("/student/index")
  
  return render_template(menupage, 
                          menus = menus, 
                         students = students, 
                         gender = gender)

@app.route("/student/add", methods=['post'])
def add_student():
  data = request.form  
  query = add_student_to_db(data)  
  flash("Murid berhasil ditambahkan")
  
  return redirect(url_for('index_student'))

  #return json.dumps(query, default=str)

@app.route("/student/update", methods=['post'])
def update_student():
  data = request.form
  query = update_student_to_db(data)
  flash("Murid berhasil diupdate")
  return redirect(url_for('index_student'))

@app.route("/student/delete", methods=['post'])
def delete_student():
  data = request.form
  query = delete_student_from_db(data)
  flash("Murid berhasil dihapus")
  return redirect(url_for('index_student'))
  #return json.dumps(query, default=str)

#@app.route("/delete/<id>", methods = ['get','post'] )
#def delete(id):
#  my_data = Data.query.get(id)
#  db.session.delete(my_data)
#  db.session.commit()
#  flash("Data deleted")
#  return redirect(url_for('hello_world'))

#login
@app.route("/login", methods=['GET', 'POST'])
def login():
  menus = load_menu_from_db()
  menupage = load_active_menu_from_db("/login")

  form = RegisterForm(request.form)
  if request.method == 'POST' and form.validate():
    #name = form.name.data
    #username = form.username.data
    #email = form.email.data
    #password = sha256_crypt.encrypt(form.password.data)
    #query = f"INSERT INTO user (name, username, email, password) VALUES ('{name}', '{username}', '{email}', '{password}')"
    #print(query)
    #return redirect(url_for('hello_world'))
  #  return json.dumps(t, default=str)
  #return json.dumps(t, default=str)
    return render_template(menupage, menus = menus)
  return render_template(menupage, 
                         menus = menus, 
                         form=form)




#register user
class RegisterForm(Form):
  name = StringField('Name', [validators.Length(min=1, max=50)])
  username = StringField('Username', [validators.Length(min=4, max=25)])
  email = StringField('Email', [validators.Length(min=6, max=50)])
  password = PasswordField('Password',[
    validators.DataRequired(),
    validators.EqualTo('confirm', message='Passwords do not match')
  ])
  confirm = PasswordField('Confirm Password')

@app.route("/register", methods=['GET', 'POST'])
def register():
  menus = load_menu_from_db()
  menupage = load_active_menu_from_db("/register")

  form = RegisterForm(request.form)
  if request.method == 'POST' and form.validate():
    #name = form.name.data
    #username = form.username.data
    #email = form.email.data
    #password = sha256_crypt.encrypt(form.password.data)
    #query = f"INSERT INTO user (name, username, email, password) VALUES ('{name}', '{username}', '{email}', '{password}')"
    #print(query)
    #return redirect(url_for('hello_world'))
  #  return json.dumps(t, default=str)
  #return json.dumps(t, default=str)
    return render_template(menupage, menus = menus)
  return render_template(menupage, 
                         menus = menus, 
                         form=form)

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