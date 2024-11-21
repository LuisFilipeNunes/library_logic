from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models.database import Session, UserModel, BookModel
from classes.user import User
from managers_utils.user_id_gen import generate_user_id


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class FlaskUser(UserMixin):
    def __init__(self, user):
        self.user = user
        self.id = user.email

    def get_id(self):
        return self.id

@login_manager.user_loader
def load_user(user_id):
    session = Session()
    user_model = session.query(UserModel).filter_by(email=user_id).first()
    session.close()
    if user_model:
        user = User(user_model.name, user_id, user_model.email, user_model.password)
        return FlaskUser(user)
    return None

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        session = Session()
        user_model = session.query(UserModel).filter_by(email=email).first()
        print("Attempted login with:", email)
        print("User found:", user_model is not None)
        if user_model:
            print("Stored hash:", user_model.password)
            print("Password check result:", check_password_hash(user_model.password, password))
        
        session.close()
        if user_model and check_password_hash(user_model.password, password):
            user = User(user_model.name, email, user_model.email, user_model.password)
            flask_user = FlaskUser(user)
            login_user(flask_user)
            return redirect(url_for('index'))
        flash('Invalid email or password')
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')
        user_id = generate_user_id()
        
        session = Session()
        if session.query(UserModel).filter_by(email=email).first():
            session.close()
            flash('Email already registered')
            return redirect(url_for('signup'))
        
        hashed_password = generate_password_hash(password)
        new_user = UserModel(
            id=user_id,
            email=email,
            name=name,
            password=hashed_password,
            booklist=''
        )
        session.add(new_user)
        session.commit()
        session.close()
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
