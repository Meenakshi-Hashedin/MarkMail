from flask import Flask, request, jsonify
from app.models import User,db
from app import app
@app.route('/hello-world')
def hello_world():
    return 'Hello world'

@app.route('/users',methods=['POST','GET','DELETE','PUT'])
def User_Data():

    if request.method == 'POST':
        username = request.args.get('username')
        email = request.args.get('email')
        user = User(username=username, email=email)
        db.session.add(user)
        db.session.commit()
        return '{}{}' .format(username, email)

    if request.method == 'GET':
        username = request.args.get('username')
        email = request.args.get('email')
        return 'userDetails {}{}' .format(username, email)

    if request.method == 'PUT':
        username = request.args.get('username')
        email = request.args.get('email')
        editName='sarada'
        user = User.query.filter_by(username=username).first()
        user.username = editName
        db.session.commit()
        return 'updated name is{}' + editName

    if request.method == 'DELETE':
        username = request.args.get('username')
        email = request.args.get('email')
        User.query.filter_by(username=username,email=email).delete()
        db.session.commit()
        return 'deleted {}' .format(username)

























