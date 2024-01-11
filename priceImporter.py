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
