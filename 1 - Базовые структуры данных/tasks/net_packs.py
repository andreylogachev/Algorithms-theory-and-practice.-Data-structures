class Buffer:
    def __init__(self, size):
        self.data = [-1]*size
        self.size = size
        self.head = 0
        self.tail = -1
        self.count = 0

    def __repr__(self):
        return self.data

    def is_full(self):
        return self.count == self.size

    def is_empty(self):
        return self.count == 0

    def enqueue(self, value):
        new_tail = (self.tail + 1) % self.size
        self.data[new_tail] = value
        self.tail = new_tail
        self.count += 1

    def top(self):
        return self.data[self.head]

    def dequeue(self):
        value = self.top()
        self.data[self.head] = -1
        self.head = (self.head + 1) % self.size
        self.count -= 1
        return value




def main():
    size, n = map(int, input().split())
    buffer = Buffer(size)
    start_times = [-1]*n
    for i in range(n):
        arrival, duration = map(int, input().split())

        # очистка очереди
        if not buffer.is_empty():
            j, dur_j = buffer.top()
            while start_times[j] + dur_j <= arrival and not buffer.is_empty():
                buffer.dequeue()
                current_time = start_times[j] + dur_j
                if not buffer.is_empty():
                    j, dur_j = buffer.top()
                    start_times[j] = current_time

        # добавление пакета
        if not buffer.is_full():
            buffer.enqueue((i, duration))
            j, dur_j = buffer.top()
            if start_times[j] == -1:
                start_times[j] = arrival

    # обработка остатка очереди
    while not buffer.is_empty():
        j, dur_j = buffer.top()
        current_time = start_times[j] + dur_j
        buffer.dequeue()
        if not buffer.is_empty():
            j, dur_j = buffer.top()
            start_times[j] = current_time

    # вывод времен начала
    print(*start_times, sep='\n')

if __name__ == "__main__":
    main()
