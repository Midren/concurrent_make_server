from flask import jsonify, request, Blueprint
from app.models import Node, User
from app import app, db

nodes = Blueprint('/nodes', __name__)


@app.route("/node_summary", methods=["GET"])
def get_summary():
    summary = db.engine.execute("select * from node_summary")
    objs = []
    for i in summary:
        obj = {}
        obj['id'] = i[0]
        obj['user_name'] = i[1]
        obj['compiler_name'] = i[2]
        obj['major_version'] = i[3]
        obj['minor_verison'] = i[4]
        obj['os_name'] = i[5]
        objs.append(obj)
    return jsonify(objs), 200


@nodes.route("", methods=["POST"])
def create_node():
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


@nodes.route("/<int:id>", methods=["PUT"])
def change_node(id):
    new_node = request.get_json()
    node = Node.query.get(id)
    node.public_key = new_node["public_key"]
    node.ip = new_node["ip"]
    db.session.commit()
    return jsonify(eval(str(new_node)))


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


@app.route("/<int:id_u>", methods=["DELETE"])
def delete(id_u):
    print(db.session.query(Node.id).all())
    if (id_u,) not in db.session.query(Node.id).all():
        return "There is no such student in database", 404

    db.session.query(Node).filter(Node.id == id_u).delete(
        synchronize_session='evaluate')
    db.session.commit()
    return "Everything fine", 200
