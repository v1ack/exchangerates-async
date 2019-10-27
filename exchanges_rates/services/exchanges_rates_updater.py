import asyncio
import json
import logging

from aiohttp import ClientSession
from aiomisc import Service

from ..models import Rates

logger = logging.getLogger(__name__)


class ExchangesRatesUpdater(Service):
    """
    Ассинхронный сервис для обновления курсов валют
    """
    rates: Rates = None
    delay: int = 60
    api_url = 'https://api.exchangeratesapi.io/latest'

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

    async def start(self):
        """
        Бесконечный цикл обновления курса

        :return: None
        """
        self.start_event.set()
        while True:
            async with ClientSession() as session:
                update = await self.fetch(session, self.api_url)
                logger.info('Exchanges rates updated')
                self.rates.set(json.loads(update))
            await asyncio.sleep(self.delay)
