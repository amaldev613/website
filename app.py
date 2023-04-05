from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'company': 'SwipeWire',
  'title': 'Data Analyst',
  'location': 'Bengaluru, India',
  'salary': 'Rs. 10,00,000'
}, {
  'id': 2,
  'company': 'Kiddily',
  'title': 'Data Scientist',
  'location': 'Delhi, India',
  'salary': 'Rs. 15,00,000'
}, {
  'id': 3,
  'company': 'Bandcamp',
  'title': 'Frontend Engineer',
  'location': 'Mumbai, India',
  'salary': 'Rs. 12,00,000'
}, {
  'id': 4,
  'company': 'Formonix',
  'title': 'Backend Engineer',
  'location': 'Kochi, India',
  'salary': 'Rs. 10,00,000'
}]


@app.route("/")
def hello_jovian():
  return render_template('home.html', jobs=JOBS)


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
