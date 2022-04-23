# Mapping Keys to Multiple Values in a Dictionary
from collections import defaultdict

def main():
    # Multiple Values as `list`
    d = defaultdict(list)
    d['a'].append(1)
    d['a'].append(1)
    d['a'].append(2)
    d['b'].append(3)
    d['b'].append(4)
    print(d) # defaultdict(<class 'list'>, {'a': [1, 1, 2], 'b': [3, 4]})

    # Multiple Values as `set`
    e = defaultdict(set)
    e['a'].add(1)
    e['a'].add(1)
    e['a'].add(2)
    e['b'].add(3)
    e['b'].add(4)
    print(e) # defaultdict(<class 'set'>, {'a': {1, 2}, 'b': {3, 4}})


if __name__ == "__main__":
    main()
