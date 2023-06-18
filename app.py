from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
load_dotenv()
import os
token = os.environ.get('password')
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:' + token + '@localhost/dummy' 
db=SQLAlchemy(app)


class Data(db.Model):
    __tablename__="products"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100),unique=True)
    info=db.Column(db.String(10000))
    price=db.Column(db.String(10))
    ingredients=db.Column(db.String(10000))
    url=db.Column(db.String(3000))
    brand=db.Column(db.String(100))
    volume=db.Column(db.String(100))
    skin=db.Column(db.String(20))

    def __init__(self, name, info, price, ingredients, url, brand, volume, skin):
        self.name=name
        self.info=info
        self.price=price
        self.ingredients=ingredients
        self.url=url
        self.brand=brand
        self.volume=volume
        self.skin=skin

@app.route("/", methods=["GET"])
def index():
    products=Data.query.all()
    return render_template("index.html", products=products)

@app.route("/dry.html", methods=['GET'])
def dry():
    products=Data.query.filter(Data.skin=='dry').all()
    return render_template("dry.html", products=products)

@app.route("/oily.html", methods=['GET'])
def oily():
    products=Data.query.filter(Data.skin=='oily').all()
    return render_template("oily.html", products=products)

@app.route("/sensitive.html", methods=['GET'])
def sensitive():
    products=Data.query.filter(Data.skin=='sensitive').all()
    return render_template("sensitive.html", products=products)

if __name__ == '__main__':
    app.debug=True
    app.run(host='0.0.0.0')