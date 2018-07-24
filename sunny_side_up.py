from flask import Flask , render_template,request
from datetime import datetime

app = Flask("MyApp")

@app.route("/")
def home():
	return render_template("homepage.html")

@app.route("/search_postcode", methods=["POST"])
def read_label_data():
	form_data = request.form
	location = form_data.get("location")
	return render_template("restaurant_page.html", location=location)


if __name__ == "__main__":
	app.run(debug=True)
