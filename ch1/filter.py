# Filtering Sequence Elements

def main():
    names = ['Cat', 'Elephant', 'Lion', 'Tiger', 'Dog', 'Leopard']

    # Filters names with more than 4 characters
    filtered = [ n for n in names if len(n) > 4 ]

    print(filtered) # ['Elephant', 'Tiger', 'Leopard']


if __name__ == "__main__":
    main()
