def selection_sort(lst):
    len_list = len(lst)
    for i in range(len_list):
        for j in range(i+1, len_list):
            if lst[j] < lst[i]:
                lst[j], lst[i] = lst[i], lst[j]
    return lst


def main():
    lists = [
        ([], []),
        ([3], [3]),
        ([3, 1, 2], [1, 2, 3]),
        ([3, 1, 2, 3, 4, 1, 2, 34], [1, 1, 2, 2, 3, 3, 4, 34]),
    ]
    for each in lists:
        assert selection_sort(each[0]) == each[1]


if __name__ == '__main__':
    main()
