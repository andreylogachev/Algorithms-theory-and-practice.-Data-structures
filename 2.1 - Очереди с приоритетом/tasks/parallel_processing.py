def sift_down(a, i):
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
        sift_down(a, min_ind)


def main():
    n, m = map(int, input().split())
    times = list(map(int, input().split()))

    # мин-куча хранящая пары: (время окончания работы, номер процессора)
    processes = [(0, i) for i in range(n)]
    for t in times:
        min_process = processes[0]
        print(min_process[1], min_process[0])
        processes[0] = min_process[0] + t, min_process[1]
        sift_down(processes, 0)


if __name__ == "__main__":
    main()
