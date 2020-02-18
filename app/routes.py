from flask import Flask,request,jsonify,make_response
from app.models import User
from app import app
@app.route('/hello-world')
def hello_world():
    return 'Hello world'



