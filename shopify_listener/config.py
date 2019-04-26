# -*- coding: utf-8 -*-
# @Author: Matthieu Petiteau
# @Date:   2019-04-17 12:15:24
# @Last Modified by:   smallwat3r
# @Last Modified time: 2019-04-26 22:08:40

"""Flask environment config."""

import os


class DefaultConfig:
    """Development."""

    DEBUG = True
    SESSION_KEY = os.getenv('FLASK_SESSION_KEY')
    HMAC_SECRET = os.getenv('HMAC_SECRET').encode()


class ProductionConfig(DefaultConfig):
    """Production."""

    DEBUG = False
    SESSION_COOKIE_SECURE = True
