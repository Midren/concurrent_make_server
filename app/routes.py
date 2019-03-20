from app import app, db
from app.models import Node
from flask import jsonify, request
import json

@app.route("/get_ips", methods=["GET"])
def get_ips():
    addresses = []
    for node in Node.query.all():
        addresses.append({"address": node.login + "@" + node.ip})
    return jsonify({"addresses": addresses})

@app.route("/get_public_keys", methods=["GET"])
def get_pk():
    pks = []
    for node in Node.query.all():
        pks.append({"public_key": node.public_key})
    return jsonify({"public_keys": pks})
