# Exchanges rates async
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

#### docker-compose

```yaml
version: '2.4'

services:
  app:
    image: v1ack/exchangerates_async:latest
    ports:
      - 8080:8080
    environment:
      APP_ADDRESS: 0.0.0.0
      APP_PORT: 8080
      EXCHANGES_UPDATE_INTERVAL: 60
```

#### docker-compose with local build

`run_app.sh`

#### pip

Installing
`pip install dist/exchanges_rates_async-0.1-py3-none-any.whl`

### Tests

#### Pytest

`pytest conftest.py`

(doesn't work on Windows)

#### Docker

`run_tests.sh`
