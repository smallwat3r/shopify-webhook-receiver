# -*- coding: utf-8 -*-
# @Author: Matthieu Petiteau
# @Date:   2019-04-26 20:59:22
# @Last Modified by:   smallwat3r
# @Last Modified time: 2019-04-26 23:08:13

"""Utils."""

import base64
import hashlib
import hmac

from . import app


def verify_webhook(data, hmac_header):
    """Verify Shopify webhook."""
    digest = hmac.new(app.config['HMAC_SECRET'], data, hashlib.sha256).digest()
    computed_hmac = base64.b64encode(digest)
    return hmac.compare_digest(computed_hmac, hmac_header.encode('utf-8'))
