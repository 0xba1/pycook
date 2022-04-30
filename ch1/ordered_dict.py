# Keeping Dictionaries in Order
from collections import OrderedDict 

def main():
    d = OrderedDict()
    d['foo'] = 1
    d['bar'] = 2
    d['baz'] = 3
    d['buz'] = 4

    # OrderedDict([('foo', 1), ('bar', 2), ('baz', 3), ('buz', 4)])
    print(d)


    # foo 1
    # bar 2
    # baz 3
    # buz 4
    for key in d:
        print(key, d[key])


if __name__ == "__main__":
    main()

