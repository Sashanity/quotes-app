
import os
from flask import Flask, render_template, request,  flash, redirect, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from dotenv import load_dotenv
app = Flask(__name__)

load_dotenv() 
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
mongo = PyMongo(app)
db=mongo.db

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        quote_text = request.form.to_dict()
        mongo.db.quotes.insert_one(quote_text)
        flash(u'New item added!', 'info')
        return redirect("/")
    else:
        quotes=list(mongo.db.quotes.find({}))      
        return render_template('index.html',quotes=quotes)

@app.route('/delete/<quote_id>')
def delete_quote(quote_id):
    quote=mongo.db.quotes.find_one({'_id': ObjectId(quote_id)})
    mongo.db.quotes.delete_one({'_id': ObjectId(quote_id)})
    flash(u'Item deleted', 'info')
    # return render_template('index.html',quotes=quotes)
    return redirect("/")

@app.route('/update/<quote_id>', methods=['GET', 'POST'])
def update_quote(quote_id):
    
    quote=mongo.db.quotes.find_one({'_id':ObjectId(quote_id)})
    if request.method == 'POST':
        quote_content = request.form.to_dict()
        mongo.db.quotes.update_one(quote,{"$set":quote_content})
        return redirect("/")
    else:
        return render_template('update.html', quote=quote)


if __name__ == "__main__":
    app.secret_key = 'some secret key'
    app.run(debug=True)
    