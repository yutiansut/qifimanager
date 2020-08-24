__version__ = '1.2.0'
__author__ = 'yutiansut'

from qifimanager.manager import QA_QIFIMANAGER, QA_QIFISMANAGER
from qifimanager.qifiwebserver import QAQIFI_Handler
from QAWebServer.QA_Web import start_server

def run_server():
    start_server([(r"/qifi", QAQIFI_Handler)], '0.0.0.0', 8019)