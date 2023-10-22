from flask import Flask, render_template, jsonify

app = Flask(__name__)

WORK = [
  {
    'id': 1,
    'title': 'Wordpress Developer',
    'location': 'Remote, Canada',
    'duration': 'Present'
  },
  {
    'id': 2,
    'title': 'Frontend Engineer',
    'location': 'Remote, Canada',
    'duration': '1 year'
  },
  {
    'id': 3,
    'title': 'Qa Analyst/Project Coordinator',
    'location': 'Remote, Ontario',
    'duration': '1 year'
  },
  {
    'id': 4,
    'title': 'Intern',
    'location': 'Remote, Ontario',
    'duration': '4 months'
  },
  {
    'id': 5,
    'title': 'Restaurant Floor Manager',
    'location': 'Vancouver, Canada'
  }
  
]


@app.route("/")
def hello_world():
    return render_template('index.html', work = WORK, name = 'Minhaj Masood')

@app.route("/api/work")
def list_work():
  return jsonify(WORK)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)