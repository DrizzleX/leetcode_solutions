def binary_search(lst, target):
    s_idx = 0
    e_idx = len(lst) - 1
    while e_idx >= s_idx:
        m_idx = (s_idx + e_idx) // 2
        if lst[m_idx] == target:
            return m_idx
        elif lst[m_idx] > target:
            e_idx = m_idx - 1
        else:
            s_idx = m_idx + 1
    return None



def main():
    lst = [1, 2, 3, 4, 5, 6, 7]
    assert binary_search(lst, 6) == 5
    assert binary_search(lst, 1) == 0
    assert binary_search(lst, 7) == 6
    assert binary_search(lst, 0) is None

    lst = [1]
    assert binary_search(lst, 1) == 0
    assert binary_search(lst, 2) is None


if __name__ == '__main__':
    main()
