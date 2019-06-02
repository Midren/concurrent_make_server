from app import app, db
from app.routes import nodes

app.register_blueprint(nodes, url_prefix="/nodes")
if __name__ == "__main__":
    app.run()