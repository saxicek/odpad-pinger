""" main.py is the top level script.

Return response from http://odpad-praha8.rhcloud.com/status
"""

import os
import sys
import json
import urllib2

# sys.path includes 'server/lib' due to appengine_config.py
from flask import Flask
from flask import jsonify
app = Flask(__name__.split('.')[0])


@app.route('/')
def ping():
    """ Return hello template at application root URL."""
    url = "http://odpad-praha8.rhcloud.com/status"
    try:
        result = urllib2.urlopen(url)
        return jsonify(json.loads(result.read()))
    except urllib2.URLError, e:
        return jsonify({'error': e.message})
