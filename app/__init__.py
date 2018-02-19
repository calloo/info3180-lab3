from flask import Flask
from flask_mail import Mail

app = Flask(__name__)

app.config['SECRET_KEY'] = 'abc123'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '465'
app.config['MAIL_USERNAME'] = '	5302aba0c87288'
app.config['MAIL_PASSWORD'] = '1ee8a121903d7e'
mail = Mail(app)
from app import views