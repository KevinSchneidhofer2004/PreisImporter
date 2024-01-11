import matplotlib.pyplot as plt
from collections import defaultdict
import numpy as np


class PriceImporter:
    def __init__(self, file):
        with open(file, encoding="utf-8") as f:
            self.data = f.read()

    def process_data(self):
        data_list = []
        lines = self.data.strip().split('\n')

        for line in lines:
            parts = line.strip().split(',')
            name, timestamp, price, currency, location = parts
            data_list.append({
                'name': name,
                'timestamp': timestamp,
                'price': float(price),
                'currency': currency,
                'location': location
            })

        print(data_list)
        return data_list

    def show_graph(self):
        data_list = self.process_data()
        data_dict = defaultdict(list)

        for entry in data_list:
            location = entry['location'].strip(';')
            data_dict[location].append(entry)

        for location, entries in data_dict.items():
            companies = [entry['name'] for entry in entries]
            prices = [entry['price'] for entry in entries]

            colors = plt.cm.viridis(np.linspace(0, 1, len(companies)))

            plt.bar(companies, prices, color=colors)
            plt.xlabel('Companies')
            plt.ylabel('Prices')
            plt.title(f'Prices in {location}')
            plt.xticks(rotation=45, ha='right')
            plt.show()
