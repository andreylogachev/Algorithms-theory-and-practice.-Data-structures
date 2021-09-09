class MaxQueue:
    """Очередь максимумов очереди"""
    def __init__(self, size):
        self.data = [-1]*size
        self.size = size
        self.head = 0
        self.tail = -1
        self.count = 0

    def __repr__(self):
        return self.data

    def __get_num(self, item):
        if not isinstance(item, int):
            raise KeyError(item)
        if 0 <= item <= self.count - 1:
            return (self.head + item) % self.size
        if -self.count <= item < 0:
            return (self.tail + 1 + item) % self.size
        return KeyError(item)

    def __getitem__(self, item):
        return self.data[self.__get_num(item)]

    def __setitem__(self, key, value):
        self.data[self.__get_num(key)] = value

    def is_full(self):
        return self.count == self.size

    def is_empty(self):
        return self.count == 0

    def enqueue(self, value):
        new_tail = (self.tail + 1) % self.size
        self.data[new_tail] = value
        self.tail = new_tail
        self.count += 1
        self.sift_up()

    def sift_up(self):
        while self.count >= 2 and self[-1] > self[-2]:
            self[-1] = self.pop_back()

    def top(self):
        return self.data[self.head]

    def dequeue(self):
        value = self.top()
        self.data[self.head] = -1
        self.head = (self.head + 1) % self.size
        self.count -= 1
        return value

    def pop_back(self):
        value, self[-1] = self[-1], -1
        self.count -= 1
        self.tail = (self.tail - 1) % self.size
        return value


def main():
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    max_queue = MaxQueue(m)
    max_on_windows = []

    for i in range(m - 1):
        max_queue.enqueue(a[i])
    for i in range(m - 1, n):
        max_queue.enqueue(a[i])
        curr_max = max_queue.top()
        # если текущий максимум выходит из окна, удаляем его из максимумов
        if curr_max == a[i - m + 1]:
            max_queue.dequeue()
        max_on_windows.append(curr_max)
    print(*max_on_windows)


if __name__ == "__main__":
    main()
