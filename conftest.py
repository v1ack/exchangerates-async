import os

import pytest
import asyncio
from aiohttp import ClientSession
from unittest.mock import Mock
import json

from exchanges_rates.models import Rates
from exchanges_rates.services import APIService, ExchangesRatesUpdater

RATES = {'RATE1': 36.65,
         'RATE2': 41.15}


@pytest.fixture
def rates():
    _rates = Rates()
    yield _rates


@pytest.fixture
def rest_port(aiomisc_unused_port_factory):
    return aiomisc_unused_port_factory()


@pytest.fixture
async def rest_service(rates, rest_port):
    return APIService(port=rest_port, rates=rates, address='localhost')


@pytest.fixture
def services(rest_service):
    return [rest_service]


async def fetch(session: ClientSession, url: str) -> tuple:
    async with session.get(url) as response:
        return await response.text(), response.status


@pytest.mark.skipif(os.name == 'nt', reason='You use windows')
async def test_api(rates, rest_port):
    rates.set({'rates': RATES})
    async with ClientSession() as session:
        response, status = await fetch(session, f'http://localhost:{rest_port}/')
        print(response)
        assert RATES == json.loads(response)['rates']

        rate = list(RATES.keys())[0]
        response, status = await fetch(session, f'http://localhost:{rest_port}/{rate}')
        assert rate == json.loads(response)['name']
        assert RATES[rate] == json.loads(response)['rate']

        response, status = await fetch(session, f'http://localhost:{rest_port}/should_be_not_found')
        assert status == 404


@pytest.mark.skipif(os.name == 'nt', reason='You use windows')
async def test_api_empty(rates, rest_port):
    async with ClientSession() as session:
        response, status = await fetch(session, f'http://localhost:{rest_port}/')
        assert status == 503

        response, status = await fetch(session, f'http://localhost:{rest_port}/should_be_not_found')
        assert status == 503


@pytest.mark.skipif(os.name == 'nt', reason='You use windows')
async def test_rates_updater(rates):
    rates.set(dict(rates={'RATES': 50}))
    ExchangesRatesUpdater.fetch = Mock(return_value=json.dumps(dict(rates={'RATES': 42})))
    loop = asyncio.get_event_loop()
    task = ExchangesRatesUpdater(interval=60, rates=rates)
    task.set_loop(loop)
    await task.start()
    await asyncio.sleep(1)
    assert rates.get('RATES') == 42


def test_rates(rates):
    assert not rates.is_set
    assert rates.get_all() == {}
    rates.set(dict(rates=RATES))
    assert rates.get_all() == RATES
    rate = list(RATES.keys())[0]
    assert rates.get(rate) == RATES[rate]
