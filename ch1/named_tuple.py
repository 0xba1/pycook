# Mapping Names to Sequence Elements

from collections import namedtuple

def main():
    Fruit = namedtuple('Fruit', ['name', 'price'])
    orange = Fruit('Orange', 1.23)

    print(orange.name) # 'Orange'
    print(orange.price) # 1.23


if __name__ == "__main__":
    main()
