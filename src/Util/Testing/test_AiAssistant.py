import unittest
from AiAssistant import CheckStockData, ask, CreateGraph  

class TestYourApp(unittest.TestCase):
    def setUp(self):
        # Set up any necessary objects or variables for testing
        pass

    def tearDown(self):
        # Clean up any resources after testing
        pass

    def test_check_stock_data(self):
        stock_data = {
            "Time Series (5min)": {
                "2023-11-22 09:30:00": {
                    "1. open": "100.00",
                    "4. close": "105.00"
                },
                "2023-11-22 09:35:00": {
                    "1. open": "110.00",
                    "4. close": "115.00"
                }
            }
        }
        result = CheckStockData(stock_data, "XYZ")
        self.assertIsInstance(result, dict)

    def test_ask(self):
        message = "How are you?"
        result = ask(message)
        self.assertIsInstance(result, dict)

    def test_create_graph(self):
        stock_data = {
            "Time Series (5min)": {
                "2023-11-22 09:30:00": {
                    "1. open": "100.00",
                    "4. close": "105.00"
                },
                "2023-11-22 09:35:00": {
                    "1. open": "110.00",
                    "4. close": "115.00"
                }
            }
        }
        result = CreateGraph(stock_data)
        self.assertIsInstance(result, dict)

if __name__ == '__main__':
    unittest.main()
