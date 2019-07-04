# shopify-flask-webhook-dispatcher

This Flask app allows to catch Shopify webhooks events and trigger actions.

## ⚙️ Set up 
To start the app, first set up a virtual environment, activate it and install the needed dependencies.

```sh
$ virtualenv -p python3 venv --no-site-package
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Create the needed environment variables.
```sh
$ export HMAC_SECRET=<shared secret signed from Shopify webhook>
$ export FLASK_ENV=<development/production>

$ export FLASK_APP=shopify_listener
```

Launch the app.
```sh
python3 -m flask run --host='0.0.0.0'
```

The activity is logged in a file `logs.log`
```
26-Apr-19 23:01:08 - Webhook topic orders/create has been processed.
26-Apr-19 23:01:08 - 104.197.39.59 - - [26/Apr/2019 23:01:08] "POST / HTTP/1.1" 200 -
26-Apr-19 23:01:18 - Webhook topic orders/create has been processed.
26-Apr-19 23:01:18 - 35.239.155.162 - - [26/Apr/2019 23:01:18] "POST / HTTP/1.1" 200 -
```

_**Hint for testing:** It's not possible to link Shopify webhooks from localhost. For testing you can use [Ngrok](https://ngrok.com/) to get a temporary domain._

## 🧩 Allocate actions to events
You can allocate different actions to do while an event is catched using the private functions in `dispatcher.py`  

**Example**  
The webhook topic `orders/create` is called.  
The `dispatch_event()` function will redirect the event to the private function `_orders_create()`.  
In this case, `_orders_create()` will retrieve the order id and customer email to send this data to an internal api.

```python
# dispatcher.py


class Dispatcher:

    # ......
    
    def _orders_create(self):
    	"""orders/create.
        
        If order created, send order id and customer email to internal API.
        """
        url = 'https://<domain>/api/<endpoint>'
        r = requests.post(url, data={'order_id': self.data['id'], 'customer_email': self.data['email']})
        return r.content
```

**Events mapped:**   
* carts/create, carts/update   
* checkouts/create, checkouts/update, checkouts/delete  
* collections/create, collections/update, collections/delete 
* collection_listings/add, collection_listings/remove, collection_listings/update  
* customers/create, customers/disable, customers/enable, customers/update, customers/delete 
* customer_groups/create, customer_groups/update, customer_groups/delete   
* draft_orders/create, draft_orders/update, draft_orders/delete   
* fulfillments/create, fulfillments/update   
* fulfillment_events/create   
* fulfillment_events/delete  
* inventory_items/create, inventory_items/update    
* inventory_items/delete   
* inventory_levels/connect, inventory_levels/update, inventory_levels/disconnect    
* locations/create, locations/update, locations/delete   
* orders/cancelled, orders/create, orders/fulfilled, orders/paid, orders/partially_fulfilled, orders/updated, orders/delete   
* order_transactions/create   
* products/create, products/update, products/delete  
* product_listings/add, product_listings/remove, product_listings/update   
* refunds/create   
* app/uninstalled, shop/update   
* tender_transactions/create     
* themes/create, themes/publish, themes/update, themes/delete   
