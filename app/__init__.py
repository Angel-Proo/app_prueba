from flask import Flask
from flask_mail import Mail
from config import Config, MailConfig

app = Flask(__name__)
app.config.from_object(Config)

mail = Mail(app)

from app.apis.routes import api_bp
from app.forms.routes import forms_bp

app.register_blueprint(api_bp, url_prefix='/api')
app.register_blueprint(forms_bp, url_prefix='/forms')