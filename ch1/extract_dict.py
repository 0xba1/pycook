# Extracting a Subset of a Dictionary


def main():
    prices = {
            'Apple': 15.24,
            'Shoe': 199.99,
            'Meat': 5.02,
            'Mango': 2.29,
            'Orange': 4.49,
            'Cream': 7.45,
            }

    fruits = ['Apple', 'Orange', 'Pineapple', 'Mango', 'Strawberry']

    fruit_prices = { key:value for key, value in prices.items() if key in fruits }

    print(fruit_prices) // {'Apple': 15.24, 'Mango': 2.29, 'Orange': 4.49}



if __name__ == "__main__":
    main()
