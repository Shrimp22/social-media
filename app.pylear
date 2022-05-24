from flask import Flask
from db import db
from auth import auth
import os
app = Flask(__name__)

app.register_blueprint(auth.bp)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./users.db'
db.init_app(app)

if not os.path.isfile('./users.db'):
    with app.app_context():
        db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
