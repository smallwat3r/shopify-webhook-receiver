# -*- coding: utf-8 -*-
# @Author: Matthieu Petiteau
# @Date:   2019-04-17 12:16:07
# @Last Modified by:   smallwat3r
# @Last Modified time: 2019-04-26 22:17:49

"""Init App."""

import os

from flask import Flask
from werkzeug.contrib.fixers import ProxyFix


app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

configurations = {
    'development': 'shopify_listener.config.DefaultConfig',
    'production': 'shopify_listener.config.ProductionConfig'
}
app.config.from_object(configurations[os.getenv('FLASK_ENV')])


import shopify_listener.views
