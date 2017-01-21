class QueueFullError(Exception):
    def __init__(self, message, errors = None):
        super(QueueFullError, self).__init__(message)

class QueueEmptyError(Exception):
    def __init__(self, message, errors = None):
        super(QueueEmptyError, self).__init__(message)

class Queue:
    def __init__(self, max_size):
        self.arr = []
        self.max_size = max_size

    def is_empty(self):
        if len(self.arr) == 0:
            return True
        return False 

    def is_full(self):
        if len(self.arr) >= self.max_size:
            return True
        return False

    def enqueue(self, element):
        if self.is_full():
            raise QueueFullError("Queue is full: cannot enqueue in a full queue")
        self.arr.append(element)

    def dequeue(self):
        if self.is_empty():
            raise QueueEmptyError("Queue is empty: cannot dequeue from an empty queue")
        elem = self.arr[len(self.arr) - 1]
        del self.arr[len(self.arr) - 1]
        return elem


if __name__ == "__main__":
    queue = Queue(15)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    value = queue.dequeue()
    print value
