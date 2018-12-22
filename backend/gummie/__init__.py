from flask import Flask
from flask_cors import CORS
from flask_mongoengine import MongoEngine


app = Flask(__name__,
            static_folder="../../dist/static",
            template_folder="../../dist")

app.config.from_object('config.Config')
db = MongoEngine(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

# company.contact_methods.append(contacts)
# company.save()
from .views import controller
