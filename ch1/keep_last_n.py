from collections import deque

# Searches a string iter for a pattern and 
# yields the element that matches the pattern in a generator and lines(history) before it
def search(str_iter, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for elem in str_iter:
        if pattern in elem:
            yield elem, previous_lines
        previous_lines.append(elem)

def main():
    cats = "cats are better than dogs.\nDon't @ me.\nOk, why dont you think so.\nAnyway, I've never seen a python before."
#    print(cats)
    for result in search(cats, "n"):
        print(result)



if __name__ == "__main__":
    main()
