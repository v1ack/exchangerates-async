import logging

from aiohttp import web
from aiomisc.service.aiohttp import AIOHTTPService

from ..models import Rates

logger = logging.getLogger(__name__)


class APIService(AIOHTTPService):
    """
    http сервер
    """
    rates: Rates = None

    async def all_rates(self, request: web.Request) -> web.Response:
        """
        Все курсы

        :param request: запрос
        :return: ответ 🙃
        """

        logger.info('Request for all currencies')
        return web.json_response(
            dict(
                rates=self.rates.get_all(),
                last_update=self.rates.last_set
            ))

    async def one_rate(self, request: web.Request) -> web.Response:
        """
        Один курс по имени

        :param request: запрос
        :return: ответ 🙃
        """
        currency = request.match_info['currency']
        logger.info('Request for %s', currency)
        rate = self.rates.get(currency)

        if rate is not None:
            return web.json_response(
                dict(
                    name=currency.upper(),
                    rate=rate,
                    last_update=self.rates.last_set
                ))

        logger.warning('Currency %s not found', currency)
        return web.HTTPNotFound()

    async def create_application(self) -> web.Application:
        """
        Создание сервера

        :return: сервер
        """
        app = web.Application()
        app.add_routes([web.get('/', self.all_rates),
                        web.get('/{currency}', self.one_rate)])
        return app
