# -*- coding: utf-8 -*-
# @Author: Matthieu Petiteau
# @Date:   2019-04-17 12:12:58
# @Last Modified by:   smallwat3r
# @Last Modified time: 2019-04-26 23:08:00

"""Webhook listener / dispatcher."""

import logging

from . import app, utils
from .dispatcher import Dispatcher

from flask import abort, request


logging.basicConfig(
    filename='logs.log',
    filemode='a',
    format='%(asctime)s - %(message)s',
    datefmt='%d-%b-%y %H:%M:%S',
    level=logging.INFO
)


@app.route('/', methods=['POST'])
def handle_webhook():
    """Handle Shopify webhooks."""
    data = request.get_data()
    verified = utils.verify_webhook(
        data, request.headers.get('X_SHOPIFY_HMAC_SHA256')
    )

    if not verified:
        logging.warning('Unauthorized connection.')
        abort(401)

    event = request.headers.get('X_SHOPIFY_TOPIC')
    Dispatcher(data).dispatch_event(event)
    logging.info('Webhook topic {} has been processed.'.format(event))

    return ('Webhook verified', 200)
