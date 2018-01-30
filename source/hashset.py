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
        return self.hashtable.keys()

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
        self.hashtable.delete(element)  # O(1), if element
        self.size -= 1

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
        union = self
        # Loop through each element in the other set
        # O(s), where s is size of otherset
        for otherset_element in other_set.elements():
            # Skip element if already in the union.
            # O(u), u is the number of all unique elements between each set.
            if union.contains(otherset_element):
                continue
            # add it to the union if not
            union.add(otherset_element)  # O(1)

        return union  # O(1)

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
        intersection = HashSet()  # O(1)
        # Loop through each element in the other set
        # O(n), where n is size of otherset
        for otherset_element in other_set.elements():
            # Add element if it appears in both sets.
            # O(i), i is the number of all unique elements between each set.
            if self.contains(otherset_element):
                intersection.add(otherset_element)  # O(1)

        return intersection  # O(1)

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
        difference = HashSet()  # O(1)
        # Loop through each element in the other set
        # O(n), where n is size of otherset
        for otherset_element in other_set.elements():
            # Skip element if it appears in both sets.
            # O(i), i is the number of all unique elements between each set.
            if self.contains(otherset_element):
                continue
            # add it if it's unique among both sets.
            difference.add(otherset_element)  # O(1)

        return difference  # O(1)
