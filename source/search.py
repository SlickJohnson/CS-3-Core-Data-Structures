#!python
"""Binary and linear search implementations."""


def linear_search(array, item):
    """Return the first index of item in array or None if item is not found."""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    if index >= len(array):
        return None

    if item == array[index]:
        return index

    return linear_search_recursive(array, item, index + 1)


def binary_search(array, item):
    """Return the index of item in sorted array or None if item is not found."""

    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    left = 0
    right = len(array) - 1

    while left <= right:
        index = (left + right) // 2

        if item == array[index]:
            return index

        if item < array[index]:
            right = index - 1
        else:
            left = index + 1

    return None


def binary_search_recursive(array, item, left=None, right=None):
    if left > right:
        return None

    index = (left + right) // 2

    if item == array[index]:
        return index

    if item < array[index]:
        return binary_search_recursive(array, item, left, index - 1)
    else:
        return binary_search_recursive(array, item, index + 1, right)
