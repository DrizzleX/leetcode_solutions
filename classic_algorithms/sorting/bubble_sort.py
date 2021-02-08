def bubble_sort(lst):
    return lst


def main():
    lists = [
        ([], []),
    ]
    for each in lists:
        assert bubble_sort(each[0]) == each[1]

if __name__ == '__main__':
    main()
