from __init__ import db

class User(db.Model):
    user_name_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(256), nullable=False)
    ips = db.relationship('Node', backref='login')
    def __repr__(self):
        return '<User ' + self.user_name + '@' + str(self.user_name_id) + '>'



class Node(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_key = db.Column(db.String(512), unique=True)
    login_id = db.Column(db.Integer, db.ForeignKey('user.user_name_id'))
    ip = db.Column(db.String(15), unique=True, nullable=False)
    def __repr__(self):
        user = User.query.filter_by(user_name_id=self.login_id).first()
        return '<Node ' + user.user_name + '@' + self.ip + '>'