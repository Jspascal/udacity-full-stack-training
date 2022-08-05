from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://josephnomo:4705@localhost:5432/blog'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(), nullable=False)
    pwd = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'<User ID : {self.id}, Full Name : {self.full_name}>'

db.create_all()

@app.route('/')
def index():
    user = User.query.first()
    return "hello " + user.full_name
