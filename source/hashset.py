#!python
"""Implementation of the Set data type."""
from hashtable import HashTable


class HashSet(object):
    """A Set data structure implemented using a HashTable."""

    def __init__(self, elements=None):
        """Initialize a new empty set, and add any given elements."""
        super().__init__()

    def elements(self):
        """Return all the elements in this set.

        Complexity:
            Best:
            Worst:

        Returns:
            list: a list containing all the elements in this set.

        """
        pass

    def length(self):
        """Return the size of this set.

        Complexity:
            Best:
            Worst:

        Returns:
            int: the size of the set.

        """
        pass

    def contains(self, element):
        """Check whether element is in this set.

        Args:
            element: any -- what to check for in the set.

        Complexity:
            Best:
            Worst:

        Returns:
            bool: whether the element is in this set.

        """
        pass

    def add(self, element):
        """Add element to this set, if not present already.

        Args:
            element: any -- what to add to this set.

        Complexity:
            Best:
            Worst:

        """
        pass

    def remove(self, element):
        """Remove element from this set, if present.

        Args:
            element: any -- the element to remove from this set.

        Complexity:
            Best:
            Worst:

        Raises:
            KeyError: if the element is not in this set.

        """
        pass

    def union(self, other_set):
        """Return a new set that is the union of this set and other_set.

        Args:
            other_set: Set -- the set that will be combined with this set.

        Complexity:
            Best:
            Worst:

        Returns:
            Set: the union of the two sets.

        """
        pass

    def intersection(self, other_set):
        """Return a new set that is the intersection of this set and other_set.

        Args:
            other_set: Set -- the set that will intersect this set.

        Complexity:
            Best:
            Worst:

        Returns:
            Set: the intersection between the two sets.

        """
        pass

    def difference(self, other_set):
        """Return a new set that is the difference of this set and other_set.

        Args:
            other_set: Set -- the set that will be compared to this set.

        Complexity:
            Best:
            Worst:

        Returns:
            Set: the difference between the two sets.

        """
        pass
