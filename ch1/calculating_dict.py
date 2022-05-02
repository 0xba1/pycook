# Calculating with dictionary

def main():
    prices = {
            'Fish': 4.23,
            'Car': 45000,
            'Cream': 10.5,
            'Table': 45.55,
    }
    min_price = min(zip(prices.values(), prices.keys()))
    max_price = max(zip(prices.values(), prices.keys()))
    prices_sorted = sorted(zip(prices.values(), prices.keys()))

    print(min_price) # (4.23, 'Fish')

    print(max_price) # (45000, 'Car')
    
    # [(4.23, 'Fish'), (10.5, 'Cream'), (45.55, 'Table'), (45000, 'Car')]
    print(prices_sorted)


if __name__ == "__main__":
    main()
