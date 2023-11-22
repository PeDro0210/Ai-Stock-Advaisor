import unittest
from StockProcess import Stock

class TestStock(unittest.TestCase):
    def setUp(self):
        self.stock = Stock("XYZ")

    def tearDown(self):
        del self.stock

    def test_symbol_searcher(self):
        result = self.stock.SymbolSearcher()
        self.assertIsInstance(result, dict)

    def test_stock_data(self):
        result = self.stock.StockData("ABC")
        self.assertIsInstance(result, dict)

    def test_del_stock(self):
        self.stock.DelStock()
        self.assertIsNone(self.stock)

if __name__ == '__main__':
    unittest.main()