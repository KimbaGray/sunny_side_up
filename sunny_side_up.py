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
	return render_template("imagegrid.html", location=location)

	# if location == "North":

	# elif

	# form_data = request.form
	# location = form_data.get("location")
	# return render_template("restaurant_page.html", location=location)
	#


if __name__ == "__main__":
	app.run(debug=True)
