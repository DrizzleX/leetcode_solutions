def selection_sort(lst):
    if not lst:
        return lst
    for i in range(len(lst)-1):
        for j in range(i+1, len(lst)):
            if lst[i] > lst[j]:
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
