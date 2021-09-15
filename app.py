from email import message
from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy
from email_send import send_email
from sqlalchemy.sql import func


app=Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:593134482@localhost:5432/height_collector'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://fxrpypvyseniin:4811c57067b16f2713cae6d0caac0633826dcd9b4f1d205eceeabea59b56ff21@ec2-52-203-74-38.compute-1.amazonaws.com:5432/d451noivp8aukc?sslmode=require'
db=SQLAlchemy(app)

class Data(db.Model):
    __tablename__="data"
    id=db.Column(db.Integer,primary_key=True)
    email_=db.Column(db.String(123),unique=True)
    height_=db.Column(db.Integer)

    def __init__(self,email_,height_):
        self.email_=email_
        self.height_=height_


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success",methods=['POST'])
def success():
    if request.method == "POST":
        email=request.form["email_name"] 
        height = request.form["height_name"]
        File=request.files["file"]
        content=File.read()
        print(content)
        return render_template("index.html")
        #sned_email(email,message)
        """ if (db.session.query(Data).filter(Data.email_==email).count())==0:
            data=Data(email,height)
            db.session.add(data)
            db.session.commit()
            avg_height=db.session.query(func.avg(Data.height_)).scalar()
            avg_height=round(avg_height)
            count=db.session.query(Data.height_).count()
            #send_email(email,avg_height,count)
            print(avg_height)
            return render_template("success.html",text=f"Hey there, the average height of {count} people is {height}")
        else:
            return render_template("index.html",text="seems like we got something wrong!!") """
@app.route("/download")
def download():
    pass
if __name__ == '__main__':
    app.debug=True
    app.run()