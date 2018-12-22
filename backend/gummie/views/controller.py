from flask import jsonify, render_template

from backend.gummie import app
from backend.models.company_info import Ghummie


# default html render for all routes.
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")


@app.route('/api/update')
def update():
    email = Ghummie.objects.find()
    return jsonify(email)


@app.route('/api/gummie/contacts')
def api():
    """
    Returns:
        Company's contacts in JSON format.
    """
    comp_contacts_list = Ghummie.objects.values_list('contact_methods')
    comp_contacts = comp_contacts_list.first()[0]
    return jsonify(comp_contacts)
