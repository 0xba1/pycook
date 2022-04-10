import heapq

# A priority queue will pop an element of the highest priority, 
# if of equal priority, based on its index.
class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        # The second argument is a tuple of which the heap will order 
        # based on the ordering of its element in ascending order, i.e,
        # first based on priority, then based on index
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        # This pops the first member of the queue(one with highest priority) 
        # then returns the last element of that tuple
        return heapq.heappop(self._queue)[-1]


def main():
    queue = PriorityQueue()
    queue.push('Sugar', 1)
    queue.push('Salt', 2)
    queue.push('Honey', 5)
    queue.push('Fish', 4)

    print(queue.pop()) # 'Honey'
    print(queue.pop()) # 'Fish'
    print(queue.pop()) # 'Salt'
    print(queue.pop()) # 'Sugar'

if __name__ == '__main__':
    main()
