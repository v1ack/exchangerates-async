# Exchanges rates asyns
Provides async http server with auto update

### REST API

#### All rates

`GET /`

    {
    	"rates": {
    		"RATE": 36.65,
    		"RATE2": 41.15 
    	},
    	"last_update" : "2019-10-28T15:09:17.071752"
    }

#### Rate for current currency

`GET /{currency}`

    {
    	"name": "RATE"
    	"rate": 36.65,
    	"last_update" : "2019-10-28T15:09:17.071752"
    }

### How to run

#### Python
```python
from exchanges_rates import run_services
run_services(address='localhost', port=8080, exchange_update_interval=60)
```