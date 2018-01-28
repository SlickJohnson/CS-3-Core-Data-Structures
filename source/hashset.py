#!python
"""Implementation of the Set data type."""
from hashtable import HashTable


class HashSet(object):
    """A Set data structure implemented using a HashTable."""

    def __init__(self, elements=None):
        """Initialize a new empty set, and add any given elements."""
        self.hashtable = HashTable()
        self.size = 0
        # Add all provided elements provided.
        if elements:
            for element in elements:
                self.add(element)

    def elements(self):
        """Return all the elements in this set.

        Complexity:
            Best:
            Worst:

        Returns:
            list: a list containing all the elements in this set.

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
        return self.hashtable.contains(element)

    def add(self, element):
        """Add element to this set, if not present already.

        Args:
            element: any -- what to add to this set.

        Complexity:
            Best:
            Worst:

        """
        if not self.contains(element):
            self.hashtable.set(element, None)
            self.size += 1

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
