class MaxStack:
    def __init__(self):
        self.data = list()
        self.max_data = list()

    def is_empty(self):
        if not self.data:
            return True
        return False

    def push(self, elem):
        self.data.append(elem)
        if len(self.max_data) == 0:
            self.max_data.append(elem)
        else:
            self.max_data.append(max(self.max_data[-1], elem))

    def top(self):
        if not self.is_empty():
            return self.data[-1]

    def pop(self):
        if not self.is_empty():
            self.max_data.pop()
            return self.data.pop()

    def max(self):
        if len(self.max_data) != 0:
            return self.max_data[-1]
        return 0


def main():
    import sys
    reader = sys.stdin
    q = int(next(reader))
    stack = MaxStack()
    for _ in range(q):
        commands = next(reader).split()
        command = commands[0]
        if command == "push":
            v = int(commands[1])
            stack.push(v)
        elif command == "pop":
            stack.pop()
        elif command == "max":
            print(stack.max())


if __name__ == "__main__":
    main()
