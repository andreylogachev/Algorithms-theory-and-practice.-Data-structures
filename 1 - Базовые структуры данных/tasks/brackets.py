class Stack:
    def __init__(self):
        self.data = list()

    def is_empty(self):
        if not self.data:
            return True
        return False

    def push(self, elem):
        self.data.append(elem)

    def top(self):
        if not self.is_empty():
            return self.data[-1]

    def pop(self):
        if not self.is_empty():
            return self.data.pop()


def check_brackets(s):
    """
    ПРоверка строки на правильно расставленные скобки.
    Решение на основе стека
    Второй стек - индекс открывающей скобки
    :param s: Строка
    :return: Если все верно - "Success", иначе индекс неправильной скобки:
    неправильной последней закрывающей или первой открывающей
    """
    stack = Stack()
    index_stack = Stack()
    brackets_pairs = {'(': ')', '[': ']', '{': '}'}
    for i, c in enumerate(s):
        if c in ('(', '[', '{'):
            stack.push(c)
            index_stack.push(i + 1)
        elif c in (')', ']', '}'):
            if stack.is_empty():
                return i + 1
            top = stack.pop()
            index_stack.pop()
            if brackets_pairs[top] != c:
                return i + 1
    if not stack.is_empty():
        return index_stack.data[0]
    return "Success"


def _main():
    s = input()
    print(check_brackets(s))


if __name__ == "__main__":
    _main()
