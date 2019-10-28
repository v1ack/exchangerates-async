import json
import logging

from aiohttp import ClientSession
from aiomisc.service.periodic import PeriodicService

from ..models import Rates

logger = logging.getLogger(__name__)


class ExchangesRatesUpdater(PeriodicService):
    """
    Ассинхронный сервис для обновления курсов валют
    """
    rates: Rates = None
    interval: int = 60
    api_url = 'https://api.ratesapi.io/api/latest'

    @staticmethod
    async def fetch(session: ClientSession, url: str) -> str:
        """
        Ассинхронный http запрос

        :param session: aiohttp сессия
        :param url: адрес
        :return: текст ответа
        """
        async with session.get(url) as response:
            return await response.text()

    async def callback(self):
        """
        Бесконечный цикл обновления курса

        :return: None
        """
        async with ClientSession() as session:
            update = await self.fetch(session, self.api_url)
            logger.info('Exchanges rates updated')
            self.rates.set(json.loads(update))
