# Combining Multiple Mappings into a Single Mappings

from collections import ChainMap

def main():
    fruit_prices_1 = {'Orange': 2.53, 'Mango': 1.85, 'Cashew': 1.23}
    fruit_prices_2 = {'Apple': 5.23, 'Orange': 3.40, 'Pineapple': 8.32}

    # If there are duplicates, first argument gets chosen e.g 'Orange' is 2.53 not 3.40
    fruit_prices = ChainMap(fruit_prices_1, fruit_prices_2)

    print(fruit_prices['Orange']) # 2.53
    print(fruit_prices['Mango']) # 1.85
    print(fruit_prices['Cashew']) # 1.23
    print(fruit_prices['Apple']) # 5.23
    print(fruit_prices['Pineapple']) # 8.32



if __name__ == "__main__":
    main()
