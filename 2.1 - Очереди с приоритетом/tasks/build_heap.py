def sift_down(a, i, swap_list):
    n = len(a)
    left_child_ind = 2 * i + 1
    right_child_ind = 2 * i + 2

    min_ind = i
    if left_child_ind < n and a[left_child_ind] < a[min_ind]:
        min_ind = left_child_ind
    if right_child_ind < n and a[right_child_ind] < a[min_ind]:
        min_ind = right_child_ind
    if min_ind != i:
        a[min_ind], a[i] = a[i], a[min_ind]
        swap_list.append((i, min_ind))
        sift_down(a, min_ind, swap_list)


def build_heap(a):
    """
    Построение мин-кучи на месте
    :param a: Массив
    :return: Куча
    """
    # 0-based heap
    n = len(a)
    swap_list = []
    for i in range((n - 1) // 2, -1, -1):
        sift_down(a, i, swap_list)
    return swap_list


def main():
    n = int(input())
    a = list(map(int, input().split()))
    swap_list = build_heap(a)
    print(len(swap_list))
    for pair in swap_list:
        print(*pair)

if __name__ == "__main__":
    main()
