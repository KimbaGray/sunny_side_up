from flask import Flask , render_template,request
from datetime import datetime

app = Flask("MyApp")

@app.route("/")
def home():
	return render_template("homepage.html")

@app.route("/howdoyoulikeyoureggs")
def eggs():
	return render_template("landingpage.html")

@app.route("/search_area", methods=["POST"])
def search_area():
	location = request.form["location"]
	if location == "Central":
		return render_template("central.html", location=location)
	elif location == "North":
		return render_template("north.html", location=location)
	else:
		return render_template("otherareas.html", location=location)

if __name__ == "__main__":
	app.run(debug=True)
