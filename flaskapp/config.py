import os
import pymysql
class Config:
    SECRET_KEY= 'd71e327c04c11549fc8889cc652e781b54669d00927627ed5ddbb8a1baf44a2c'
    CKEDITOR_ENABLE_CODESNIPPET = True
    SQLALCHEMY_DATABASE_URI =  "sqlite:///ayoub.db"
       #'mysql+pymysql://youssef:pythonicyoussef@localhost/ayoub_db'
    #'postgres://pdoiadhnevckkg:223bf9332939941fb3fb1fe974b883ae0ceb20499178774b1e5167fcbf35a889@ec2-44-205-112-253.compute-1.amazonaws.com:5432/de6adjfvm5puh4'
    #'mysql+pymysql://youssef:pythonicyoussef@localhost/ayoub_db'
    #"sqlite:///ayoub.db"

    SQLALCHEMY_POOL_RECYCLE = 280
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_ADMIN_SWATCH = 'cerulean'
    CKEDITOR_ENABLE_CODESNIPPET = True
    CKEDITOR_FILE_UPLOADER = 'users.upload'

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
    MAIL_USE_SSL = False