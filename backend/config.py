import os

# Define the application directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    DEBUG = True
    TESTING = False
    SECRET_KEY = 'BBr9FA3PeVJQu4XHV1LztbRMBk'

    MONGODB_SETTINGS = {
        'db': 'Ghummie',
        'host': 'localhost'
    }
