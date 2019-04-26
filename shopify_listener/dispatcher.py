# -*- coding: utf-8 -*-
# @Author: Matthieu Petiteau
# @Date:   2019-04-26 21:01:07
# @Last Modified by:   Matthieu Petiteau
# @Last Modified time: 2019-04-26 21:52:46

"""Dispatch webhook event to specific actions."""


class Dispatcher:
    """Dispatch the different webhook events to the related functions.

    The list of all webhook events can be found at:
    https://help.shopify.com/en/api/reference/events/webhook
    """

    def __init__(self, data):
        """Init webhook data."""
        self.data = data

    @staticmethod
    def name_topic(topic):
        """Rename the topic event to match the function names."""
        return "_" + topic.replace('/', '_')

    def dispatch_event(self, topic):
        """Dispatch the event to the correct function."""
        return getattr(self, self.name_topic(topic))()

    def _carts_create(self):
        pass

    def _carts_update(self):
        pass

    def _checkout_create(self):
        pass

    def _checkout_update(self):
        pass

    def _checkout_delete(self):
        pass

    def _collections_create(self):
        pass

    def _collections_update(self):
        pass

    def _collections_delete(self):
        pass

    def _collection_listings_add(self):
        pass

    def _collection_listings_remove(self):
        pass

    def _collection_listings_update(self):
        pass

    def _customers_create(self):
        pass

    def _customers_disable(self):
        pass

    def _customers_enable(self):
        pass

    def _customers_update(self):
        pass

    def _customers_delete(self):
        pass

    def _customer_groups_create(self):
        pass

    def _customer_groups_update(self):
        pass

    def _customer_groups_delete(self):
        pass

    def _draft_orders_create(self):
        pass

    def _draft_orders_update(self):
        pass

    def _draft_orders_delete(self):
        pass

    def _fulfillments_create(self):
        pass

    def _fulfillments_update(self):
        pass

    def _fulfillment_events_create(self):
        pass

    def _fulfillment_events_delete(self):
        pass

    def _inventory_items_create(self):
        pass

    def _inventory_items_update(self):
        pass

    def _inventory_items_delete(self):
        pass

    def _inventory_levels_connect(self):
        pass

    def _inventory_levels_update(self):
        pass

    def _inventory_levels_disconnect(self):
        pass

    def _locations_create(self):
        pass

    def _locations_update(self):
        pass

    def _locations_delete(self):
        pass

    def _orders_cancelled(self):
        pass

    def _orders_create(self):
        pass

    def _orders_fulfilled(self):
        pass

    def _orders_paid(self):
        pass

    def _orders_partially_fulfilled(self):
        pass

    def _orders_updated(self):
        pass

    def _orders_delete(self):
        pass

    def _orders_transactions_create(self):
        pass

    def _products_create(self):
        pass

    def _products_update(self):
        pass

    def _products_delete(self):
        pass

    def _product_listings_add(self):
        pass

    def _product_listings_remove(self):
        pass

    def _product_listings_update(self):
        pass

    def _refund_create(self):
        pass

    def _app_uninstalled(self):
        pass

    def _shop_update(self):
        pass

    def _tender_transactions_create(self):
        pass

    def _themes_create(self):
        pass

    def _theme_publish(self):
        pass

    def _theme_update(self):
        pass

    def _theme_delete(self):
        pass
