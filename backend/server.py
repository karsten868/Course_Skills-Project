from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import json
app=Flask(__name__)

#global variable holder 
holder= {}

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:peacelove@localhost/course_database'

db = SQLAlchemy(app)

db.init_app(app)
db.create_all(app=app)


@app.route("/test", methods=['GET'])
def test():
    return {"test": ["test1","test2","test3"]}



@app.route("/api/data",methods=['POST'])
def receive_data():
    global holder
    # Access the data sent in the request
    
    # Handle POST request
    holder= request.get_json()
    return type(holder)
        
    
@app.route("/api/data",methods=['GET'])
def display_data():
    global holder
    return holder
        



   





if __name__ == "__main__" :
    app.run(debug=True)