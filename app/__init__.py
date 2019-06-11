
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ip.db'
db = SQLAlchemy(app)
import routes, models
app.register_blueprint(routes.nodes, url_prefix='/nodes')