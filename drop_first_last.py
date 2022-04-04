def drop_first_last(iter):
    _, *rest, _ = iter
    return rest

def main():
    print(drop_first_last((1, 2, 3, 4, 5)))
    print(drop_first_last([1, 2, 3, 4, 5]))


if __name__ == "__main__":
    main()
