import multiprocessing
import time
import unittest
import api_server

class ApiServerUnittest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.api_server_process = multiprocessing.Process(
          target=api_server.app.run
        )
        cls.api_server_process.start()
        time.sleep(0.1)

    @classmethod
    def tearDownClass(cls):
        cls.api_server_process.terminate()
    