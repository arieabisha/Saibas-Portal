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
    result = conn.execute(text("select * from jobs where id = :val"), {"val": id})    
  rows = []
  for row in result.all():
    rows.append(row)    
  return rows  
      
    
    


