from flask import Flask
import os
app = Flask(__name__)
     
@app.route("/")
def index():
	return "Welcome to the index page."

@app.route("/hi/")
def who():
	return "who are you?"

@app.route("/hi/<username>")
def greet(username):
	return "Hi there, " + username + " !!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))	