import os

class Config:
    SECRET_KEY = '0a06aa9e6c708306b30d048a8b67aa10'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'

    # configurations for flask_email
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
