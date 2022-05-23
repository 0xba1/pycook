# Splitting Strings on Multiple Delimiters

import re

def main():
    line = 'What    , is    this'

    words = re.split(r'\W+', line)

    print(words) # ['What', 'is', 'this']

if __name__ == "__main__":
    main()
