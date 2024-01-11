from priceImporter import PriceImporter

importer = PriceImporter('test_data.csv')

importer.process_data()
importer.show_graph()
