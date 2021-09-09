class DJSet:
    """
    Класс системы непересекающихся множеств.
    Элементы - набор различных чисел п/п.
    """
    def __init__(self, n):
        self.parents = [-1]*n
        self.rank = [0]*n

    def make_set(self, i):
        self.parents[i] = i

    def find(self, x):
        # эвристика сжатия путей
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        x_id, y_id = self.find(x), self.find(y)
        if x_id == y_id:
            return
        if self.rank[x_id] > self.rank[y_id]:
            self.parents[y_id] = x_id
            return

        self.parents[x_id] = y_id
        if self.rank[x_id] == self.rank[y_id]:
            self.rank[y_id] += 1
        return


class Tables(DJSet):
    """
    Класс системы непересекающихся множеств
    с поодержкой максимума по множествам.
    Элементы - набор различных чисел п/п - номера таблиц.
    """
    def __init__(self, n):
        super().__init__(n)
        self.sizes = [0]*n
        self.max_size = 0

    def make_set(self, i, size):
        super().make_set(i)
        self.sizes[i] = size
        self.max_size = max(self.max_size, size)

    def union(self, x, y):
        x_id, y_id = self.find(x), self.find(y)
        if x_id == y_id:
            return
        if self.rank[x_id] > self.rank[y_id]:
            self.parents[y_id] = x_id
            self.sizes[x_id] += self.sizes[y_id]
            self.max_size = max(self.max_size, self.sizes[x_id])
            return

        self.parents[x_id] = y_id
        self.sizes[y_id] += self.sizes[x_id]
        self.max_size = max(self.max_size, self.sizes[y_id])
        if self.rank[x_id] == self.rank[y_id]:
            self.rank[y_id] += 1
        return


def main():
    n, m = map(int, input().split())
    tables = Tables(n)
    for i, size in enumerate(map(int, input().split())):
        tables.make_set(i, size)

    for _ in range(m):
        source, destination = map(int, input().split())
        # 1-based to 0-based indexing
        tables.union(source - 1, destination - 1)
        print(tables.max_size)


if __name__ == "__main__":
    main()
