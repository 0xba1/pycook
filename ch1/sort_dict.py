# Sorting a List of Dictionary by a Common Key

from operator import itemgetter

def main():
    rows = [
            {'name': 'apple', 'price': 100},
            {'name': 'orange', 'price': 102},
            {'name': 'mango', 'price': 92},
            {'name': 'pineaple', 'price': 98},
            {'name': 'tangerine', 'price': 52}
    ]

    rows_by_name = sorted(rows, key=itemgetter('name'))
    rows_by_price = sorted(rows, key=itemgetter('price'))

    # [{'name': 'apple', 'price': 100}, {'name': 'mango', 'price': 92}, {'name': 'orange', 'price': 102}, {'name': 'pineaple', 'price': 98}, {'name': 'tangerine', 'price': 52}]
    print(rows_by_name)

    # [{'name': 'tangerine', 'price': 52}, {'name': 'mango', 'price': 92}, {'name': 'pineaple', 'price': 98}, {'name': 'apple', 'price': 100}, {'name': 'orange', 'price': 102}]
    print(rows_by_price)


if __name__ == "__main__":
    main()
