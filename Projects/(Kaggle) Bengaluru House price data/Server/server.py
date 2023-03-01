from flask import Flask, request, jsonify
import util
import sklearn
app = Flask(__name__)

@app.route('/get_location_names')
def get_location_names():
    response =jsonify({'locations':util.get_location_names()})
    return "Hi"

if __name__ =="__main__":
    print("Starting Python Server for Home Prediction")
    app.run()