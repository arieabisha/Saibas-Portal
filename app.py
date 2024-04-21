from flask import Flask, render_template, jsonify
from database import engine, load_jobs_from_db, load_job_from_db


app = Flask(__name__)

@app.route("/")
def hello_world():
  jobs = load_jobs_from_db()
  return render_template('home.html', 
                         jobs = jobs, 
                         company_name = 'Saibas')

@app.route("/jobs")
def list_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)  

@app.route("/job/<id>")
def show_job(id):
  job = []
  job = load_job_from_db(id)
  return None

if __name__ == '__main__' :
  app.run(host='0.0.0.0',debug=True)