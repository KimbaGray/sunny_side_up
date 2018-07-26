from flask import Flask , render_template,request
from datetime import datetime

app = Flask("MyApp")

@app.route("/")
def home():
	return render_template("landingpage.html")

@app.route("/search_area", methods=["POST"])
def search_area():
	location = request.form["location"]
	return render_template("north.html", location=location)

@app.route("/homepage", methods=["POST"])
def search_area():
	return render_template("homepage.html")


	# form_data = request.form
	# location = form_data.get("location")
	# return render_template("restaurant_page.html", location=location)
	#


if __name__ == "__main__":
	app.run(debug=True)
