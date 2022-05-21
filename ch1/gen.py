# Transforming and Reducing Data at the Same Time

def main():
    prices = {
            'Orange': 1.25,
            'Avocado': 7.52,
            'Apple': 3.55,
            'Mango': 2.3,
            'Pineapple': 5.05,
            }
    
    max_price = max(price for price in prices.values())
    print(max_price) // 7.52

if __name__ == "__main__":
    main()
