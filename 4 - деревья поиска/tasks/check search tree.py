import sys
sys.setrecursionlimit(200000)


class BinaryTree:
    """Двоичное дерево"""
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

    def check(self):
        if len(self.key) == 0:
            return True
        return self._check_subtree(0)[0]

    def _check_subtree(self, i):
        left_child, right_child, key = self.left[i], self.right[i], self.key[i]
        left_min, left_max = key, key - 1
        right_min, right_max = key + 1, key

        if left_child != -1:
            status_left, left_min, left_max = self._check_subtree(left_child)
            if not status_left:
                return False, left_min, right_max

        if right_child != -1:
            status_right, right_min, right_max = self._check_subtree(right_child)
            if not status_right:
                return False, left_min, right_max

        if not left_max < key < right_min:
            return False, left_min, right_max
        return True, left_min, right_max


def main():
    n = int(input())
    bin_tree = BinaryTree(n)
    for i in range(n):
        key, left, right = map(int, input().split())
        bin_tree.add_vertex(i, key, left, right)
    if bin_tree.check():
        print("CORRECT")
    else:
        print("INCORRECT")


if __name__ == "__main__":
    main()
