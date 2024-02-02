from flask import Flask , render_template , send_from_directory
import os

app = Flask(__name__)

@app.route("/")

def home():

	return render_template("home.html")

@app.route("/how_to_use")


def how_to_use():

	return render_template("how_to_use.html")


@app.route("/how_it_works")


def how_it_works():

	return render_template("how_it_works.html")

@app.route("/contact_us")

def contact_us():

	return render_template("contact_us.html")

@app.route("/download")

def downolad():

	return send_from_directory(directory=os.getcwd()+"/static",path = "XGhostSpammer.zip")



if __name__ == "__main__" :

	app.run(debug = True , host = "localhost" , port = 80)
