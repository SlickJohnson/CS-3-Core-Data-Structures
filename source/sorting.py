#!python
from binarytree import BinarySearchTree

def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # Empty or 1 element arrays are already sorted.
    if len(items) <= 1:
        return True

    # Loop through the array.
    for index in range(len(items) - 1):
        # Check if the current element pair is out of order.
        if items[index] > items[index + 1]:
            return False

    # Array is sorted.
    return True


def _swap(items, left_index, right_index):
    """Swap the items of the given indexes.

    Args:
        left: int -- the item that's on the left side of the swap.
        right: int -- the item that's on the right side of the swap.
    """
    # Grab items at index.
    left = items[left_index]
    right = items[right_index]
    # Swap items.
    items[left_index] = right
    items[right_index] = left


def bubble_sort(items):
    """Sort items using bubble sort.

    Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted orderself.

    Args:
        items: list -- the items that will be sorted in ascending order.
    """
    # Empty or 1 element arrays are already sorted.
    if len(items) <= 1:
        return
    # Loop until the array is sorted (no swaps).
    swaps = 0
    # Set last_sorted item to last item in array on first iteration.
    last_sorted = len(items)
    while True:
        # Loop through the  array.
        for index in range(last_sorted - 1):
            # Reset swaps for new iteration.
            swaps = 0
            # Get number pair.
            left = items[index]
            right = items[index + 1]
            # Check to see if pair is out of order.
            if left > right:
                # Swap elements
                _swap(items, index, index + 1)
                swaps += 1
        # Update last sorted item index.
        last_sorted = index + 1
        # Check if done sorting.
        if swaps <= 0:
            # End loop.
            return


def selection_sort(items):
    """Sort items using selection sort.

    Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.

    Args:
        items: list -- items that will be sorted in ascending order using
            selection sort.
    """
    # Repeat until all items are in sorted order.
    for unsorted_index, unsorted_item in enumerate(items):
        # Keep track of the index of the lowest value found.
        min_index = unsorted_index
        # Loop throught items starting from fist unsorted item.
        for index in range(unsorted_index, len(items)):
            # Update index_of_min if a lower value is found.
            if items[index] < items[min_index]:
                min_index = index
        # Swap min item with first unsorted item.
        _swap(items, min_index, unsorted_index)


def insertion_sort(items):
    """Sort items using insertion sort.

    Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.

    Args:
        items: list -- items that will be sorted in ascending order using
            insertion sort.
    """
    # Repeat until all items are in sorted order
    for item in items:
        pass
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items


def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # Create new list to store sorted items.
    sorted_list = []
    # Repeat until one list is empty.
    while items1 and items2:
        # Find min item in both lists.
        items1_min = items1[0]
        items2_min = items2[0]
        # Append min items in sorted order.
        if items1_min > items2_min:
            sorted_list.append(items2_min)
            items2.pop(0)
        else:
            sorted_list.append(items1_min)
            items1.pop(0)
    # Append remaining items in non-empty list to new list.
    sorted_list.extend(items1 if items1 else items2)
    # Return result of merge.
    return sorted_list


def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # Split items list into approximately equal halves
    middle = len(items) // 2
    left = items[:middle]
    right = items[middle:]
    print('left{}, right{}', left, right)
    # Sort each half using any other sorting algorithm
    selection_sort(left)
    selection_sort(right)
    print('selection_sort_left{}, right{}', left, right)
    # Merge sorted halves into one list in sorted order
    items[:] = merge(left, right)


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if list is so small it's already sorted (base case)
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half by recursively calling merge sort
    # TODO: Merge sorted halves into one list in sorted order
    split_sort_merge(items)


def tree_sort(items):
    """Sort items using a binary tree."""
    # Put all items into a binary tree.
    tree = BinarySearchTree(items)
    # Update given items with sorted list.
    items[:] = tree.items_in_order()


def random_ints(count=20, min=1, max=50):
    """Return a list of `count` integers sampled uniformly at random from
    given range [`min`...`max`] with replacement (duplicates are allowed)."""
    import random
    return [random.randint(min, max) for _ in range(count)]


def test_sorting(sort=bubble_sort, num_items=20, max_value=50):
    """Test sorting algorithms with a small list of random items."""
    # Create a list of items randomly sampled from range [1...max_value]
    items = random_ints(num_items, 1, max_value)
    print('Initial items: {!r}'.format(items))
    print('Sorted order?  {!r}'.format(is_sorted(items)))

    # Change this sort variable to the sorting algorithm you want to test
    # sort = bubble_sort
    print('Sorting items with {}(items)'.format(sort.__name__))
    sort(items)
    print('Sorted items:  {!r}'.format(items))
    print('Sorted order?  {!r}'.format(is_sorted(items)))


def main():
    """Read command-line arguments and test sorting algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name

    if len(args) == 0:
        script = sys.argv[0]  # Get script file name
        print('Usage: {} sort num max'.format(script))
        print('Test sorting algorithm `sort` with a list of `num` integers')
        print('    randomly sampled from the range [1...`max`] (inclusive)')
        print('\nExample: {} bubble_sort 10 20'.format(script))
        print('Initial items: [3, 15, 4, 7, 20, 6, 18, 11, 9, 7]')
        print('Sorting items with bubble_sort(items)')
        print('Sorted items:  [3, 4, 6, 7, 7, 9, 11, 15, 18, 20]')
        return

    # Get sort function by name
    if len(args) >= 1:
        sort_name = args[0]
        # Terrible hack abusing globals
        if sort_name in globals():
            sort_function = globals()[sort_name]
        else:
            # Don't explode, just warn user and show list of sorting functions
            print('Sorting function {!r} does not exist'.format(sort_name))
            print('Available sorting functions:')
            for name in globals():
                if name.find('sort') >= 0:
                    print('    {}'.format(name))
            return

    # Get num_items and max_value, but don't explode if input is not an integer
    try:
        num_items = int(args[1]) if len(args) >= 2 else 20
        max_value = int(args[2]) if len(args) >= 3 else 50
        # print('Num items: {}, max value: {}'.format(num_items, max_value))
    except ValueError:
        print('Integer required for `num` and `max` command-line arguments')
        return

    # Test sort function
    test_sorting(sort_function, num_items, max_value)


if __name__ == '__main__':
    main()
