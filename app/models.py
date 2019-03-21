from __init__ import db

class Node(db.Model):
    public_key = db.Column(db.String(512), unique=True, primary_key=True)
    login = db.Column(db.String(256), nullable=False)
    ip = db.Column(db.String(15), unique=True, nullable=False)
    def __repr__(self):
        return '<Node ' + self.login + '@' + self.ip + '>'
