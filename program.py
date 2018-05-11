import csv
import os

try:
    import statistics
except:
    import statistics_standin_py2 as statistics

from data_types import Purchase


def main():
    print_header()
    filename = get_file_path()
    data = load_file(filename)
    data_search_query(data)


def print_header():
    print('----------------------------')
    print('     REAL ESTATE APP')
    print('----------------------------')
    print()


def get_file_path():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, 'Data', 'SacramentoRealEstateTransactions2008.csv')


def load_file(filename):
    with open(filename, 'r', encoding='utf-8') as fin:
        reader = csv.DictReader(fin)
        purchases = []
        for row in reader:
            p = Purchase.create_from_dict(row)
            purchases.append(p)

        return purchases


def data_search_query(data):
    data.sort(key=lambda p: p.price)
    highest_value = data[-1]
    lowest_value = data[0]
    print('The highest value property is ${:,}.'.format(round(highest_value.price)))
    print('The lowest value property is ${:,}.'.format(round(lowest_value.price)))

    all_house_prices = (
        p.price
        for p in data
    )
    average_value = statistics.mean(all_house_prices)
    print('The average value for a property is ${:,}.'.format(int(average_value)))

    two_bed_homes = [
        p
        for p in data
        if p.beds == 2
    ]

    average_two_bed_price = statistics.mean(p.price for p in two_bed_homes)
    average_two_bed_sq__ft = statistics.mean(p.sq__ft for p in two_bed_homes)
    average_two_bed_baths = statistics.mean(p.baths for p in two_bed_homes)

    print('The average two bed house is ${:,} and is {} square feet with {} bath(s).'
          .format(int(average_two_bed_price), int(average_two_bed_sq__ft), int(average_two_bed_baths)))

    sacramento_residential = [
        p
        for p in data
        if p.type.lower() == 'residential' and p.city.lower() == 'sacramento'
    ]

    average_price = statistics.mean(p.price for p in sacramento_residential)
    max_beds = max(p.beds for p in sacramento_residential)
    max_sq__ft = max(p.sq__ft for p in sacramento_residential)

    print('The average price for a Residential home in Sacramento is ${:,}.'
          ' The most beds in a Sacramento Residential is {} '
          'and the largest square footage is {}.'
          .format(round(average_price, 2), max_beds, max_sq__ft))


if __name__ == '__main__':
    main()
