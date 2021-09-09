class ChainHashTable:
    """Хэширование цепочками. Полиномиальная хэш функция на строках"""
    p = 1_000_000_007
    x = 263
    x_pow_i_list = [1, x]

    def __init__(self, m):
        self.data = [[] for i in range(m)]
        self.m = m

    def x_pow_i(self, i):
        n = len(self.x_pow_i_list)
        if i >= n:
            for j in range(n, i + 1):
                x_pow_j = self.x_pow_i_list[-1] * self.x % self.p
                self.x_pow_i_list.append(x_pow_j)
        return self.x_pow_i_list[i]

    def hash(self, s):
        return sum(ord(s[i]) * self.x_pow_i(i) for i in range(len(s))) % self.p % self.m

    def add_string(self, s):
        i = self.hash(s)
        if s not in self.data[i]:
            self.data[i].append(s)

    def del_string(self, s):
        i = self.hash(s)
        if s in self.data[i]:
            self.data[i].remove(s)

    def find_string(self, s):
        i = self.hash(s)
        if s in self.data[i]:
            print('yes')
        else:
            print('no')

    def check(self, i):
        print(" ".join(reversed(self.data[i])))


def main():
    m = int(input())
    cht = ChainHashTable(m)
    n = int(input())
    for _ in range(n):
        command, string = input().split()
        if command == 'check':
            i = int(string)
            cht.check(i)
        elif command == 'add':
            cht.add_string(string)
        elif command == 'del':
            cht.del_string(string)
        elif command == 'find':
            cht.find_string(string)


if __name__ == "__main__":
    main()
