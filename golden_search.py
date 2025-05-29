def golden_search(
    array, 
    value, 
    a=0, 
    b=None, 
    prev_x1=None,
    prev_x2=None
):
    if b is None:
        b = len(array)

    if abs(b - a) == 0:
        return int((a + b) / 2)
        
    phi = (1 + 5**0.5) / 2

    if prev_x1 is None:
        x1 = int(b - (b - a) / phi)
    else:
        x1 = prev_x1

    if prev_x2 is None:
        x2 = int(a + (b - a) / phi)
    else:
        x2 = prev_x2
        
    if array[x1] == value:
        return x1
    elif array[x2] == value:
        return x2
    elif value < array[x1]:
        return golden_search(array, value, a, x1, None, x1)
    elif value > array[x2]:
        return golden_search(array, value, x2, b, x2, None)
    else:
        return golden_search(array, value, x1, x2, x2, None)


def test_golden_search():
    # Test case 1: Basic search in sorted array
    arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert golden_search(arr1, 5) == 4
    assert golden_search(arr1, 1) == 0
    assert golden_search(arr1, 10) == 9

    # Test case 2: Search in array with repeated elements
    arr2 = [1, 2, 2, 2, 3, 3, 4, 4, 4, 5]
    assert golden_search(arr2, 2) in [1, 2, 3]
    assert golden_search(arr2, 4) in [6, 7, 8]

    # Test case 3: Search in array with single element
    arr3 = [1]
    assert golden_search(arr3, 1) == 0

    # Test case 4: Search in large sorted array
    arr4 = list(range(1000))
    assert golden_search(arr4, 500) == 500
    assert golden_search(arr4, 501) == 501
    assert golden_search(arr4, 499) == 499
    assert golden_search(arr4, 502) == 502
    assert golden_search(arr4, 498) == 498
    assert golden_search(arr4, 503) == 503
    assert golden_search(arr4, 497) == 497
    assert golden_search(arr4, 504) == 504
    assert golden_search(arr4, 496) == 496
    assert golden_search(arr4, 505) == 505
    assert golden_search(arr4, 999) == 999
    assert golden_search(arr4, 0) == 0

    print("All test cases passed!")

# Run the tests
if __name__ == "__main__":
    test_golden_search()

