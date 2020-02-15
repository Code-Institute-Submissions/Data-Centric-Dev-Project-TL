import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env

app = Flask(__name__)
app.config["MONGODB_NAME"] = os.environ.get('MONGODB_NAME')
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')
mongo = PyMongo(app)

DBS_NAME = "animal_facts"


'''
mammals = mongo.db.animals.find({"animal_type": "Mammals"})
birds = mongo.db.animals.find({"animal_type": "Birds"})
reptiles = mongo.db.animals.find({"animal_type": "Reptiles"})
amphibians = mongo.db.animals.find({"animal_type": "Amphibians"})
fish = mongo.db.animals.find({"animal_type": "Fish"})
invertebrates = mongo.db.animals.find({"animal_type": "Invertebrates"})
'''


@app.route("/")
@app.route("/get_animals")
def get_animals():
    mammals = mongo.db.animals.find({"animal_type": "Mammals"})
    birds = mongo.db.animals.find({"animal_type": "Birds"})
    reptiles = mongo.db.animals.find({"animal_type": "Reptiles"})
    amphibians = mongo.db.animals.find({"animal_type": "Amphibians"})
    fish = mongo.db.animals.find({"animal_type": "Fish"})
    invertebrates = mongo.db.animals.find({"animal_type": "Invertebrates"})
    return render_template("animals.html", mammals=mammals, birds=birds, 
                           reptiles=reptiles, amphibians=amphibians, fish=fish, 
                           invertebrates=invertebrates)


# testing piece of code
@app.route("/testing")
def testing():
    return render_template("testing.html")


@app.route("/add_animals")
def add_animals():
    return render_template("addanimal.html", categories=mongo.db.animal_types.find())


if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
