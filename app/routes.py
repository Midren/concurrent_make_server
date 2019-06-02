from flask import jsonify, request
from app.models import Node, User
from app import app, db
from flask.views import MethodView


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
    form = request.get_json()
    public_key = form["public_key"]
    ip = form["ip"]
    login = form["login"]
    user = User.query.filter_by(user_name=login).first()
    if not user:
        user = User(user_name=login)
        db.session.add(user)
        db.session.commit()
    user = User.query.filter_by(user_name=login).first()
    user_list = Node.query.filter_by(public_key=public_key).all()
    if not len(user_list):
        node = Node(public_key=public_key, ip=ip, login=user)
        db.session.add(node)
        db.session.commit()
    else:
        user_list[0].ip = ip
        user_list[0].login = user
        db.session.commit()
    return "Posted", 200


@app.route("/<int:id_u>", methods=["DELETE"])
def delete(id_u):
    print(db.session.query(Node.id).all())
    if (id_u,) not in db.session.query(Node.id).all():
        return "There is no such student in database", 404

    db.session.query(Node).filter(Node.id == id_u).delete(
        synchronize_session='evaluate')
    db.session.commit()
    return "Everything fine", 200
