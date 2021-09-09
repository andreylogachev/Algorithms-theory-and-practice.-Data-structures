def _height(child, parents, heights):
    """
    Высота для дерева, оканчивающегося в child
    :param child: Текущий узел
    :param parents: Массив родителей
    :param heights: Массив-кэш высот
    :return:
    """
    # если не известна высота
    if heights[child] == -1:
        parent = parents[child]

        # если корень
        if parent == -1:
            heights[child] = 1
        else:
            heights[child] = _height(parent, parents, heights) + 1

    return heights[child]


def tree_height(parents):
    """
    Возвращает высотку дерева
    :param parents: Список родителей для каждого узла
    :return: Высота дерева
    """
    # массив с
    heights = [-1]*len(parents)
    max_height = 1
    for child in range(len(parents)):
        max_height = max(max_height, _height(child, parents, heights))
    return max_height


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(tree_height(parents))


if __name__ == "__main__":
    main()
