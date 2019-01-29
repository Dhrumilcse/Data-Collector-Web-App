#Import dependencies
from flask import Flask, render_template

#Create instance of Flask App
app = Flask(__name__)

#Define Route and Contant of that page
@app.route("/")
def index():
    return render_template("index.html")

#Define 2nd Route and Content
@app.route("/success", methods = ['POST'])
def success():
    return render_template("success.html")

#Running and Controlling the script
if (__name__ =="__main__"):
    app.run(debug=True)
