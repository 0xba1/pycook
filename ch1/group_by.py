# Grouping Records Together Based on a Field

def main():
    from operator import itemgetter
    from itertools import groupby

    rows = [
            { 'thing': 'Shoes', 'name': 'Adidas' },
            { 'thing': 'Fruit', 'name': 'Mango' },
            { 'thing': 'Utility', 'name': 'Fan' },
            { 'thing': 'Shoes', 'name': 'Nike' },
            { 'thing': 'Fruit', 'name': 'Orange' },
            { 'thing': 'Shoes', 'name': 'Reebok' }
            ]
    # It is important to sort the field to be grouped by first
    rows.sort(key=itemgetter('thing'))

    grouped = groupby(rows, key=itemgetter('thing'))
    
    # Fruit
    #      {'thing': 'Fruit', 'name': 'Mango'}
    #      {'thing': 'Fruit', 'name': 'Orange'}
    # Shoes
    #      {'thing': 'Shoes', 'name': 'Adidas'}
    #      {'thing': 'Shoes', 'name': 'Nike'}
    #      {'thing': 'Shoes', 'name': 'Reebok'}
    # Utility
    #      {'thing': 'Utility', 'name': 'Fan'}
    for thing, items in grouped:
        print(thing)
        for i in items:
            print('     ', i)


if __name__ == "__main__":
    main()
