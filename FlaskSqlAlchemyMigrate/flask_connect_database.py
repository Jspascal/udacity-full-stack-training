from flask import Flask, render_template, redirect, request, url_for, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://josephnomo:4705@localhost:5432/blog'
db = SQLAlchemy(app)
dbmigrate = Migrate(app, db)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(32), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    posts = db.relationship('Post', backref='users', lazy=True)

    def __repr__(self):
        return f'<User Id : {self.id}, Username : {self.username}>'

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(128), nullable=False)
    content = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<Post Id : {self.id}, Title : {self.title}>'

@app.route('/signup', methods=['GET'])
def show_signup():
    return render_template('sign_up_form.html')

@app.route('/signup/submit', methods=['POST'])
def submit_signup():
    body = {}
    error = False
    try:
        json_data = request.json
        username = json_data['username']
        app.logger.info(request.get_json('username'))
        password = json_data['password']
        app.logger.info(password)
        user = User(username=username)
        user.set_password(password)
        body['username'] = user.username
        db.session.add(user)
        db.session.commit()
    except:
        error = True
        db.session.rollback()
        print(sys.exc_info())

    finally:
        db.session.close()
        if error == True:
            abort(400)
        else:
            body['success'] = True
            return jsonify(body)



