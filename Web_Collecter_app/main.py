from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy.sql import func

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres123@localhost/height_collecter'
db = SQLAlchemy(app)

class Data(db.Model):
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique = True)
    height = db.Column(db.Integer)

    def __init__(self, email, height):
        self.email = email
        self.height = height

def saveToDB(email, height):
    data = Data(email, height)
    db.session.add(data)
    db.session.commit()

def updateDB(email, height):
    db.session.query(Data).filter(Data.email == email).update({Data.height: height}, synchronize_session=False)
    db.session.commit()


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=['POST'])
def success():
    if request.method == "POST":
        email = request.form["email_name"]
        height = request.form['height_name']
        print(email, height)

        if db.session.query(Data).filter(Data.email == email).count() == 0:
            saveToDB(email, height)
        else:
            updateDB(email, height)

        height_average = db.session.query(func.avg(Data.height)).scalar()
        height_average = round(height_average, 1)
        count = db.session.query(Data.height).count()
        print(height_average, count)
        send_email(email, height, height_average, count)

        return render_template("success.html")


if __name__ == "__main__":
    app.debug = True
    app.run(port=5001)