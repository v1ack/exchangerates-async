from aiomisc.log import basic_config
import logging
from .app import run_services

basic_config(level=logging.INFO, buffered=True, log_format='color')
