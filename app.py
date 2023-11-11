from flask import Flask, jsonify, render_template
from database import load_work_from_db

app = Flask(__name__)

@app.route("/")
def hello_world():
  work = load_work_from_db()
  return render_template('index.html', work = work, name = 'Minhaj Masood')

@app.route("/api/work")
def list_work():
  work = load_work_from_db()
  return jsonify(work)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)