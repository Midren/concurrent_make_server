from __init__ import db


class Compiler(db.Model):
    compiler_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    compiler_name = db.Column(db.String(20), unique=True)
    major_version = db.Column(db.Integer, nullable=False)
    minor_version = db.Column(db.Integer, nullable=False)
    db.UniqueConstraint("major_version", "minor_version", "compiler_name", name="compiler_exists")
    computer = db.relationship('Computer', backref='compiler_name')


class Os(db.Model):
    os_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    os_name = db.Column(db.String(255), unique=True)
    computer_id = db.relationship('Computer', backref='os_name')


class Computer(db.Model):
    computer_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    compiler_id = db.Column(db.Integer, db.ForeignKey('compiler.compiler_id'))
    os_id = db.Column(db.Integer, db.ForeignKey('os.os_id'))
    pc_node = db.relationship('Node', backref='node_computer')


class User(db.Model):
    user_name_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(255), nullable=False)
    ips = db.relationship('Node', backref='login')

    def __repr__(self):
        return '<User ' + self.user_name + '@' + str(self.user_name_id) + '>'


class Node(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_key = db.Column(db.String(512), unique=True)
    login_id = db.Column(db.Integer, db.ForeignKey('user.user_name_id'))
    computer_id = db.Column(db.Integer, db.ForeignKey('computer.computer_id'))
    ip = db.Column(db.String(15), unique=True, nullable=False)

    def __repr__(self):
        user = User.query.filter_by(user_name_id=self.login_id).first()
        return '<Node ' + user.user_name + '@' + self.ip + '>'
