#!/usr/bin/python3
'''initialize flask aplication'''
from flask import Flask, Blueprint, jsonify
from flask_cors import CORS
from api.v1.views import app_views
from models import storage
from os import getenv as env

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})
app.url_map.strict_slashes = False
app.register_blueprint(app_views)


@app.errorhandler(404)
def return_error(e):
    ''' Return error not found in json format '''
    return jsonify({'error': 'Not found'}), 404


@app.teardown_appcontext
def close_teardown(error):
    '''call storage.close() in error case'''
    storage.close()


if __name__ == "__main__":
    host = "0.0.0.0"
    port = 5000
    if env("HBNB_API_HOST"):
        host = env("HBNB_API_HOST")
    if env("HBNB_API_PORT"):
        port = int(env("HBNB_API_PORT"))
    app.run(host=host, port=port, threaded=True)