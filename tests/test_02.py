import unittest
from unittest.mock import patch
import io
import matplotlib.pyplot as plt
from priceImporter import PriceImporter


class TestPriceImporter(unittest.TestCase):

    def test_show_graph(self):
        test_instance = PriceImporter("test_mock_data.csv")

        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            plt.show = lambda: None

            test_instance.show_graph()

            output = mock_stdout.getvalue()

        self.assertIn("Company_1", output)
        self.assertIn("Company_2", output)
        self.assertIn("Company_3", output)
        self.assertIn("Dublin", output)
        self.assertIn("170447132", output)
        self.assertIn("Frankfurt", output)
        self.assertIn("EUR", output)
        self.assertIn("34.27", output)


if __name__ == '__main__':
    unittest.main()
