from flask import Flask, render_template
import requests
import datetime as dt
app = Flask('app')

@app.route('/')
def pedor():
	r = requests.get("https://script.google.com/macros/s/AKfycbxim1y5h9u-SitfTC9JwlKDb3NOlRgmu3ZYczUWRc_JrT_H9DhLQeC3Hi9cFsLsCxsB9Q/exec", {"f":"board"})
	return render_template("index.html", enumerate=enumerate, users=sorted(r.json()["people"], key=lambda x: (x["points"], len(x["who"])), reverse=True))

@app.route('/data/<Name>')
def deagramm(Name):
	r = requests.get("https://script.google.com/macros/s/AKfycbxim1y5h9u-SitfTC9JwlKDb3NOlRgmu3ZYczUWRc_JrT_H9DhLQeC3Hi9cFsLsCxsB9Q/exec", {"f":"find", "name":Name})
	data = r.json()
	times = list(map(lambda x: x["time"], data))
	points = list(map(lambda x: x["points"], data))
	n = 0
	h = []
	for i in points:
		n += i
		h.append(n)
	print(times)
	return render_template("chart.html", enumerate=enumerate, dt=dt, Name=Name, data=data, times=times, points=h)

app.run(host='0.0.0.0', port=8080)