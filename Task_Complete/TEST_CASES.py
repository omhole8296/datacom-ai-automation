import unittest
from process_data import DataProcessor


class TestDataProcessor(unittest.TestCase):

    def setUp(self):
        self.processor = DataProcessor("customers.csv")
        self.processor.load_data()

    def test_export_csv(self):
        result = self.processor.export_customer_data("test_output.csv", "csv")
        self.assertTrue(result)

    def test_export_json(self):
        result = self.processor.export_customer_data("test_output.json", "json")
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()