class PhoneBook:
    """Хэш таблица с прямой адресацией для операций телефонной книги"""
    def __init__(self):
        self.data = [(-1, 'not found')] * 100000
        self.count = 0
        self.size = 100000

    def hash(self, num):
        return num % self.size

    def allocation(self):
        pass

    def _ind(self, num):
        i = self.hash(num)
        while self.data[i][0] != num and self.data[i][0] != -1:
            i = (i + 1) % self.size
        return i

    def add_number(self, num, name):
        i = self._ind(num)
        self.data[i] = num, name

    def find_number(self, num):
        i = self._ind(num)
        return self.data[i][1]

    def del_number(self, num):
        i = self._ind(num)
        self.data[i] = (self.data[i][0], 'not found')


def main():
    phone_book = PhoneBook()
    n = int(input())
    for _ in range(n):
        command_data = list(input().split())
        command, number = command_data[0].strip(), int(command_data[1])
        if command == 'add':
            name = command_data[2]
            phone_book.add_number(number, name)
        elif command == 'find':
            print(phone_book.find_number(number))
        elif command == 'del':
            phone_book.del_number(number)


if __name__ == "__main__":
    main()
