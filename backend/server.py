from flask import Flask, request
import json
app=Flask(__name__)

#global variable holder 
holder= {}


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