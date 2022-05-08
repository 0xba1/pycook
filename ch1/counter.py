# Determining the Most Frequently Occuring Items In A Sequence

from collections import Counter

def main():
    words = ['lorem', 'ipsum', 'vat', 'cum', 'ipsum', 'la', 'vat', 'lorem', 'lorem', 'vat', 'cum', 'la', 'la', 'lorem']
    count = Counter(words)
    print(count) # Counter({'lorem': 4, 'vat': 3, 'la': 3, 'ipsum': 2, 'cum': 2})
    print(count.most_common(1)) # [('lorem', 4)]
    print(count.most_common(3)) # [('lorem', 4), ('vat', 3), ('la', 3)]


if __name__ == "__main__":
    main()
