def index_power(array, n):
    """
        Find Nth power of the element with index N.
    """
    if n >= len(array):
        return -1
    if n == 0:
        return 1
    x = array[n]
    res = x
    for i in range (1, n):
        res *= x
    return res

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print(index_power([1, 2, 3, 4], 2))
    print(index_power([1, 3, 10, 100], 3))
    print(index_power([0, 1], 0))
    print(index_power([1, 2], 3))

    assert index_power([1, 2, 3, 4], 2) == 9, "Square"
    assert index_power([1, 3, 10, 100], 3) == 1000000, "Cube"
    assert index_power([0, 1], 0) == 1, "Zero power"
    assert index_power([1, 2], 3) == -1, "IndexError"
