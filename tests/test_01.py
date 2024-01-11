import unittest
from priceImporter import PriceImporter


class TestPriceImporter(unittest.TestCase):
    def test_preis_importer(self):
        test_data = "./test_data.csv"

        test_instance = PriceImporter(test_data)
        processed_test_data = test_instance.process_data()

        self.assertEqual(len(processed_test_data), 4)
        self.assertEqual(int(processed_test_data[0]['timestamp']), 170447112)
        self.assertEqual(processed_test_data[1]['name'], 'Andritz')


if __name__ == '__main__':
    unittest.main()
