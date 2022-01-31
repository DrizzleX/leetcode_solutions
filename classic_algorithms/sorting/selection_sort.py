def selection_sort(lst):
    if not lst:
        return lst
    for i in range(len(lst)-1):
        for j in range(i+1, len(lst)):
            if lst[i] > lst[j]:
                lst[j], lst[i] = lst[i], lst[j]
    return lst



def main():
    lst = [7, 2, 4, 1, 2, 1, 2, 3, 4, 5, 6, 7]
    sorted_lst = sorted(lst)
    assert selection_sort(lst) == sorted_lst
    lst = [1]
    assert selection_sort(lst) == [1]


if __name__ == '__main__':
    main()
