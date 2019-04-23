from __init__ import app, db
from models import Node, User
from flask import jsonify, request

@app.route("/get_ips", methods=["GET"])
def get_ips():
    addresses = []
    for node in Node.query.all():
        user = User.query.filter_by(user_name_id=node.login_id).first()
        addresses.append({"address": user.user_name + "@" + node.ip})
    return jsonify({"addresses": addresses})

@app.route("/get_public_keys", methods=["GET"])
def get_pk():
    pks = []
    for node in Node.query.all():
        pks.append({"public_key": node.public_key})
    return jsonify({"public_keys": pks})

@app.route("/", methods=["POST"])
def post():

    public_key = request.form["public_key"]
    ip = request.form["ip"]
    login = request.form["login"]
    user = User.query.filter_by(user_name=login).first()
    if (user is None):
        user = User(user_name=login)
        db.session.add(user)
        db.session.commit()
    user = User.query.filter_by(user_name=login).first()
    user_list = Node.query.filter_by(public_key=public_key).all()
    if not len(user_list) :
        node = Node(public_key=public_key, ip=ip, login=user)
        db.session.add(node)
        db.session.commit()
    else:
        print(user_list)
        user_list[0].ip = ip
        user_list[0].login = user
        db.session.commit()
    return "OK"

    