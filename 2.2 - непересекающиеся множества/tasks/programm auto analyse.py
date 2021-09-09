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


def main():
    n, e, d = map(int, input().split())

    # инициализация системы непересекающихся множеств
    vars = DJSet(n)
    for i in range(n):
        vars.make_set(i)

    # чтение равенств
    for _ in range(e):
        i, j = map(int, input().split())
        vars.union(i - 1, j - 1)

    # чтение неравенств
    for _ in range(d):
        i, j = map(int, input().split())
        i_id, j_id = vars.find(i - 1), vars.find(j - 1)
        if i_id == j_id:
            print(0)
            return
    print(1)
    return


if __name__ == "__main__":
    main()

