# Removing Duplicates from a Sequence while Maintaining Order

def main():
    a = [ {'x': 1, 'y': 2}, { 'x': 1, 'y': 3 }, { 'x': 1, 'y': 2 }, { 'x': 2, 'y': 4 } ]
    # [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 2, 'y': 4}]
    print(list(dedup(a, key= lambda d: (d['x'], d['y']))))

    b = [5, 1, 2, 5, 7, 6, 9, 4, 1]
    print(list(dedup(b))) # [5, 1, 2, 7, 6, 9, 4]


def dedup(items, key=None):
    seen = set()
    for item in items:
        val = item if key is  None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


if __name__ == "__main__":
    main()
