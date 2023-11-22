import unittest
from unittest.mock import patch
from flask import Flask
from flask_testing import TestCase
from StockAPI import app 
import json

class TestYourApp(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_symbol_searcher_route(self):
        response = self.client.get('/SymbolSearcher/XYZ')
        self.assertEqual(response.status_code, 200)

    def test_stock_data_route(self):
        response = self.client.get('/StockData/ABC')
        self.assertEqual(response.status_code, 200)
   
    def test_del_stock_route(self):
        response = self.client.get('/DelStock/DEF')
        self.assertEqual(response.status_code, 200)

    def test_ask_ai_route(self):
        response = self.client.get('/AskAI/How are you?')
        self.assertEqual(response.status_code, 200)
     
    def test_check_stock_data_route(self):
        response = self.client.get('/CheckStockData/GHI')
        self.assertEqual(response.status_code, 200)
      
if __name__ == '__main__':
    unittest.main()
