from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "Rani"
password = "123"
facebook_friends=["Loai","Yonathan","Adan", "George", "Fouad", "Celina", "Ayoub", "Zain", "Boulos", "Siwar", "Elena", "Sarah", "Shiraz", "Oded", "Yanay"]


@app.route('/', methods=['GET','POST'])  # '/' for the default page
def login():
	if request.method == "POST":
		username1=request.form['username']
		password1=request.form["password"]
		if username == username1 and password==password1:
			return redirect(url_for('home'))
	else:
		return render_template('login.html')

@app.route('/home',)
def home():
	return render_template("home.html", facebook_friends=facebook_friends)
@app.route('/friendexists/<string:name>')
def amigo(name):
	if name in facebook_friends:
		results=True
	else:
		results=False
	return render_template('friend_exists.html', name=name, results=results)

if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)