import logging

from aiomisc import entrypoint

from .models import Rates
from .services import ExchangesRatesUpdater, APIService

logger = logging.getLogger(__name__)


def run_services(address: str = 'localhost', port: int = 8080, exchange_update_interval: int = 60):
    rates = Rates()

    with entrypoint(APIService(address=address, port=port, rates=rates),
                    ExchangesRatesUpdater(rates=rates, interval=exchange_update_interval)) as loop:
        logger.info('Services started')
        loop.run_forever()
