import os

# Define the application directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    DEBUG = True
    TESTING = False
    SECRET_KEY = ''

    MONGODB_SETTINGS = {
        'db': 'Ghummie',
        'host': 'localhost'
    }
