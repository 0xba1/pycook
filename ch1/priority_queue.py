import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
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
