from flask import Flask , render_template,request
from datetime import datetime

app = Flask("MyApp")

#Default route this method will be called when you hit http://127.0.0.0:5000/
@app.route("/")
def home():
	return render_template("homepage.html") # render_template method is a special function flask which redirect to the html file mentioned in the paramter

@app.route("/search_postcode", methods=["POST"])
def read_label_data():
	label_data = request.label #Getting hold of a Form object that is sent from a browser.
	calculate_location =  label_data["location"] # from the form object getting value of dob field.
	location= calculate_location(area) #Calling internal method which takes year as a paramter and return text


if __name__ == "__main__":
	app.run(debug=True)
