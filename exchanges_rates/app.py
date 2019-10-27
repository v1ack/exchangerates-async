import logging

from aiomisc import entrypoint

from .models import Rates
from .services import ExchangesRatesUpdater, APIService

logger = logging.getLogger(__name__)


def run_services(address: str = 'localhost', port: int = 8080):
    rates = Rates()

    with entrypoint(APIService(address=address, port=port, rates=rates),
                    ExchangesRatesUpdater(rates=rates)) as loop:
        logger.info('Services started')
        loop.run_forever()
