from flask import Flask
from db import db
from auth import user_menagament, auth
import os
from flask_session import Session
app = Flask(__name__)

app.register_blueprint(auth.bp)
app.register_blueprint(user_menagament.bp)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./users.db'
app.config['SESSION_PERMAMENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'
db.init_app(app)
Session(app)
if not os.path.isfile('./users.db'):
    with app.app_context():
        db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
