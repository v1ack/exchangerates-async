import os

from exchanges_rates import run_services

address = os.getenv('APP_ADDRESS') or 'localhost'
port = int(os.getenv('APP_PORT', '8080'))
interval = int(os.getenv('EXCHANGES_UPDATE_INTERVAL', '60'))
run_services(address=address, port=port, exchange_update_interval=interval)
