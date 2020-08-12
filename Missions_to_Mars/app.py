from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars


app = Flask(__name__)


mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")



@app.route("/")
def home():


    mars_data = mongo.db.collection.find_one()


    return render_template("index.html", theinformation=mars_data)



@app.route("/scrape")
def scrape():


    thedata = scrape_mars.scrape() 

    # The returned data by the function has to be in dictionary format, to be inserted into MongoDB.

    mongo.db.collection.update({}, thedata, upsert=True)


    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
