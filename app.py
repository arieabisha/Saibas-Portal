from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Preschool Teacher',
    'location': 'Jakarta, Indonesia',
    'salary': 'IDR 6.000.000 - IDR 9.000.000'
  },
  {
    'id': 1,
    'title': 'PE Teacher',
    'location': 'Jakarta, Indonesia',
    'salary': 'IDR 8.000.000 - IDR 11.000.000'
  },
  {
    'id': 1,
    'title': 'Web developer',
    'location': 'Jakarta, Indonesia',
    'salary': 'IDR 11.000.000 - IDR 14.000.000'
  }
]



@app.route("/")

def hello_world():
  return render_template('home.html', jobs=JOBS , company_name='Saibas')

@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)  

if __name__ == '__main__' :
  app.run(host='0.0.0.0',debug=True)