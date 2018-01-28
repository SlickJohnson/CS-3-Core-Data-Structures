#!python
"""Tests for HashSet data stuctures."""
from hashset import HashSet
import unittest


class HashSetTest(unittest.TestCase):
    """Test HashSet implemented using a HashTable."""

    def test_init(self):
        """Initialize HashSet and check to see if default values are set."""
        st = HashSet(['a','b'])
        assert st.size == 2

    def test_elements(self):
        """Check if a list of items in the HashSet can be retrieved."""
        st = HashSet()
        assert st.elements() == []
        st.add('A')
        assert st.elements() == ['A']
        st.add('tiny')
        self.assertCountEqual(st.elements(), ['A', 'tiny'])
        st.add('set')
        self.assertCountEqual(st.elements(), ['A', 'tiny', 'set'])

    def test_length(self):
        """Check if the length is updated properly."""
        st = HashSet()
        assert st.size == 0
        st.add('check')
        assert st.size == 1
        st.add('set')
        assert st.size == 2
        st.add('size')
        assert st.size == 3

    def test_contains(self):
        """Check to see if the contains method works as intended."""
        st = HashSet()
        st.add('Hello')
        st.add('are')
        st.add('you')
        st.add('a')
        st.add('set')
        assert st.contains('Hello') is True
        assert st.contains('no') is False
        assert st.contains('you') is True
        assert st.contains('are') is True

    def test_remove(self):
        """Check to see if items can be removed from the HashSet."""
        st = HashSet()
        st.add('Please')
        st.add('dont')
        st.add('remove')
        st.add('me')
        assert st.size == 4
        st.remove('Please')
        st.remove('dont')
        assert st.size == 2
        self.assertCountEqual(st.elements(), ['remove', 'me'])
        st.remove('me')
        assert st.size == 1
        with self.assertRaises(KeyError):
            st.remove('NOOOO')

    def test_union(self):
        """Check if the union operation works as intended."""
        pass

    def test_intersection(self):
        """Check if the intersection operation works as intended."""
        pass

    def test_difference(self):
        """Check if the difference operation works as intended."""
        pass
