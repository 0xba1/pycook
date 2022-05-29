# Matching Strings Using Shell Wildcard Patterns

from fnmatch import fnmatch, fnmatchcase

def main():
    # fnmatch case sensitivity depends on host os, 
    # windows - case insensitive
    # unix - case sensitive
    print(fnmatch('goop.txt', '*.txt')) # True     

    # fnmatchcase is an always case sensitive version of fnmatch
    print(fnmatchcase('goop.txt', '*.TXT')) # False


if __name__ == "__main__":
    main()
