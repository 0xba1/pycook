# Finding commonalities in two dictionaries

def main():
    a = {
        'w': 7,
        'x': 3,
        'y': 2,
        'z': 5,
    }
    b = {
            'x': 2,
            'y': 2,
            'z': 10,
    }

    print(a.keys() & b.keys()) # {'y', 'x', 'z'}
    print(a.keys() - b.keys()) # {'w'}
    print(a.items() & b.items()) # {('y', 2)}
    print(a.items() - b.items()) # {('z', 5), ('w', 7), ('x', 3)}

    c = {key:a[key] for key in a.keys() - {'w'}}
    print(c) # {'y': 2, 'x': 3, 'z': 5}

if __name__ == "__main__":
    main()
