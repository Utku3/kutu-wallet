import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'expenses.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = 'df1/2Koo.9pL%F' # random