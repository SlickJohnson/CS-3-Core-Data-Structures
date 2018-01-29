#!python
"""Tehashsets for HashSet data hashsetuctures."""
import unittest
from hashset import HashSet


class HashSetTest(unittest.TestCase):
    """Test HashSet implemented using a HashTable."""

    def test_init(self):
        """Initialize HashSet and check to see if default values are hashset."""
        hashset = HashSet(['a', 'b'])
        assert hashset.size == 2

    def test_elements(self):
        """Check if a hashset of items in the HashSet can be retrieved."""
        hashset = HashSet()
        assert hashset.elements() == []
        hashset.add('A')
        assert hashset.elements() == ['A']
        hashset.add('tiny')
        self.assertCountEqual(hashset.elements(), ['A', 'tiny'])
        hashset.add('hashset')
        self.assertCountEqual(hashset.elements(), ['A', 'tiny', 'hashset'])

    def test_size(self):
        """Check if the length is updated properly."""
        hashset = HashSet()
        assert hashset.size == 0
        hashset.add('check')
        assert hashset.size == 1
        hashset.add('hashset')
        assert hashset.size == 2
        hashset.add('size')
        assert hashset.size == 3

    def test_contains(self):
        """Check to see if the contains method works as intended."""
        hashset = HashSet()
        hashset.add('Hello')
        hashset.add('are')
        hashset.add('you')
        hashset.add('a')
        hashset.add('hashset')
        assert hashset.contains('Hello') is True
        assert hashset.contains('no') is False
        assert hashset.contains('you') is True
        assert hashset.contains('are') is True

    def test_remove(self):
        """Check to see if items can be removed from the HashSet."""
        hashset = HashSet()
        hashset.add('Please')
        hashset.add('dont')
        hashset.add('remove')
        hashset.add('me')
        assert hashset.size == 4
        hashset.remove('Please')
        hashset.remove('dont')
        assert hashset.size == 2
        self.assertCountEqual(hashset.elements(), ['remove', 'me'])
        hashset.remove('me')
        assert hashset.size == 1
        with self.assertRaises(KeyError):
            hashset.remove('NOOOO')

    def test_union(self):
        """Check if the union operation works as intended."""
        hashset = HashSet()
        hashset.add('FUSION!')
        hashset.add('HA!')
        other_hashset = HashSet()
        other_hashset.add('HA!')
        hashset.add('FUSION!')
        union = hashset.union(other_hashset)
        assert union.size == 2
        assert union.contains('FUSION!') is True
        assert union.contains('HA!') is True

    def test_intersection(self):
        """Check if the intersection operation works as intended."""
        hashset = HashSet()
        hashset.add('Hash')
        hashset.add('Set')
        other_hashset = HashSet()
        other_hashset.add('Linked')
        other_hashset.add('Set')
        intersection = hashset.intersection(other_hashset)
        assert intersection.size == 1
        assert intersection.contains('Hash') is False
        assert intersection.contains('Set') is True
        assert intersection.contains('Linked') is False

    def test_difference(self):
        """Check if the difference operation works as intended."""
        hashset = HashSet()
        other_hashset = HashSet()
        # Spot the difference:
        hashset.add('o')
        hashset.add('o')
        hashset.add('o')
        hashset.add('o')
        other_hashset.add('O')
        other_hashset.add('o')
        other_hashset.add('o')
        other_hashset.add('o')
        other_hashset.add('o')
        difference = hashset.difference(other_hashset)
        assert difference.size == 1
        assert difference.contains('o') is False
        assert difference.contains('O') is True
