from logging import debug
from flask import Flask, render_template

app = Flask(__name__, template_folder="resource")

@app.route("/")
def home():
    # return "Home page"
    # return render_template("home.html")
    return render_template("sub_home.html")

@app.route("/about/")
def about():
    # return "Content from about"
    # return render_template("about.html")
    return render_template("sub_about.html")

if __name__ == "__main__":
    app.run(debug=True)