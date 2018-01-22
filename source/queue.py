#!python
"""Implementation of Queue data structure."""
from linkedlist import LinkedList


class LinkedQueue(object):
    """Queue implemented using a linkedlist.

    Attributes:
        list: LinkedList -- stores the queue.

    """

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any.

        Args:
            iterable: iterable -- items to put in the queue.
        """
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        return self.list.is_empty()

    def length(self):
        """Return the number of items in this queue."""
        return self.list.length()

    def enqueue(self, item):
        """Insert the given item at the back of this queue.

        Args:
            item: anytype -- what to put in the queue.

        Performance:
            Best/Worst: O(1), linkedlist appending requires only a few
                operations.

        """
        self.list.append(item)  # O(1)

    def front(self):
        """Return the item at the front of this queue without removing it.

        Returns:
            front: anytype -- the first item in the queue.

        Performance:
            Best/Worst: O(1), the front can be accessed through the variable
                'head' in the linkedlist.

        """
        front = self.list.head  # O(1)
        if front:  # O(1)
            return front.data  # O(1)

        # Queue is empty, return None.
        return None  # O(1)

    def dequeue(self):
        """Remove and return the item at the front of this queue.

        Returns:
            front: anytype -- the first item in the queue.

        Raises:
            ValueError: If queue is empty.

        """
        if self.is_empty():
            raise ValueError('Empty queue')

        front = self.list.head.data  # O(1)
        self.list.delete(front)  # O(1)

        return front  # O(1)


class ArrayQueue(object):
    """Queue implemented using an array.

    Attributes:
        list: list -- stores the queue.

    """

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any.

        Args:
            iterable: iterable -- items to put in the queue.
        """
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        return self.length() == 0

    def length(self):
        """Return the number of items in this queue."""
        return len(self.list)

    def enqueue(self, item):
        """Insert the given item at the back of this queue.

        Args:
            item: anytype -- what to put in the queue.

        Performance:
            Best/Worst: O(1), linkedlist appending requires only a few
                operations.

        """
        self.list.append(item)

    def front(self):
        """Return the item at the front of this queue without removing it.

        Returns:
            front: anytype -- the first item in the queue.

        Performance:
            Best/Worst: O(1), the front can be accessed through the variable
                'head' in the linkedlist.

        """
        # Return None if stack is empty.
        if self.is_empty():  # O(1)
            return None  # O(1)

        return self.list[0]  # O(1)

    def dequeue(self):
        """Remove and return the item at the front of this queue.

        Returns:
            front: anytype -- the first item in the queue.

        Raises:
            ValueError: If queue is empty.

        """
        if self.is_empty():  # O(1)
            raise ValueError('Empty queue')  # O(1)

        front = self.front()  # O(1)
        self.list.remove(front)  # O(n)

        return front


# Implement LinkedQueue and ArrayQueue above, then change the assignment below
# to use each of your Queue implementations to verify they each pass all tests
Queue = ArrayQueue
# Queue = ArrayQueue
