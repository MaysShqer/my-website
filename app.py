from flask import Flask, render_template
import random
app = Flask(__name__)


@app.route('/qouts')
def qouts():
	qouts=["You've got a heart as loud as lions So why let your voice be tamed?","Maybe were a little different There's no need to be ashamed","You've got the light to fight the shadows So stop hiding it away"]
	return (random.choice(qouts))


@app.route('/About Me.html')
def About_Me():
	return render_template("About Me.html")

@app.route('/contact me.html')
def contact_me():
	return render_template("contact me.html")

@app.route('/project.html')
def project_html():
	return render_template("project.html")

@app.route('/sth.html')
def sth_html():
	return render_template("sth.html")

@app.route('/superstars')
def superstar():
	superstar=["jkjah"]
	display = False
	return render_template("superstars.html",display=display, list=superstar)
		


if __name__ == "__main__":
	app.run()