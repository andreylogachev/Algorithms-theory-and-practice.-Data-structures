class BinaryTree:
    """Двоичное дерево"""
    # def __init__(self, keys, left_list, right_list):
    #     # 0 - корень
    #     n = len(keys)
    #     self.key = keys   # значение вершины
    #     self.parent = [-1]*n
    #     self.left = [-1]*n
    #     self.right = [-1]*n
    #     for parent, child in enumerate(left_list):
    #         self.left[parent] = self.child
    #         self.parent[child] = parent
    #     for parent, child in enumerate(right_list):
    #         self.right[parent] = self.child
    #         self.parent[child] = parent


    def __init__(self, n):
        self.key = [-1]*n   # значение вершины
        self.parent = [-1]*n
        self.left = [-1]*n
        self.right = [-1]*n

    def add_vertex(self, i, key, left, right):
        self.key[i] = key
        self.left[i] = left
        self.parent[left] = i
        self.right[i] = right
        self.parent[right] = i

    def in_order(self, i):
        left_child, right_child = self.left[i], self.right[i]
        if left_child != -1:
            self.in_order(left_child)
        print(self.key[i], end=' ')
        if right_child != -1:
            self.in_order(right_child)
        if i == 0:
            print()

    def pre_order(self, i):
        left_child, right_child = self.left[i], self.right[i]
        print(self.key[i], end=' ')
        if left_child != -1:
            self.pre_order(left_child)
        if right_child != -1:
            self.pre_order(right_child)
        if i == 0:
            print()

    def post_order(self, i):
        left_child, right_child = self.left[i], self.right[i]
        if left_child != -1:
            self.post_order(left_child)
        if right_child != -1:
            self.post_order(right_child)
        print(self.key[i], end=' ')
        if i == 0:
            print()


def main():
    n = int(input())
    bin_tree = BinaryTree(n)
    for i in range(n):
        key, left, right = map(int, input().split())
        bin_tree.add_vertex(i, key, left, right)

    bin_tree.in_order(0)
    bin_tree.pre_order(0)
    bin_tree.post_order(0)


if __name__ == "__main__":
    main()
