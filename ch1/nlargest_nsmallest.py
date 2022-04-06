import heapq

def nlargest(iterable, n=1, key=lambda s: s):
    return heapq.nlargest(n, iterable, key=key)

def nsmallest(iterable, n=1, key=lambda s: s):
    return heapq.nsmallest(n, iterable, key=key)

def main():
    print(nlargest([1, 2, 3, 4]))
    print(nsmallest([1, 2, 3, 4]))
    
    print(nlargest([1, 2, 3, 4], 2))
    print(nsmallest([1, 2, 3, 4], 2))

    print(nlargest([(0, 1), (1, 2), (2, 3), (3, 4)], 2, key=lambda s: s[0]))
    print(nsmallest([(0, 1), (1, 2), (2, 3), (3, 4)], 2, key=lambda s: s[0]))

if __name__ == "__main__":
    main()
