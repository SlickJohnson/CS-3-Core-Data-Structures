#!python
"""Tests for Set data stuctures."""
from set_hashtable import Set
import unittest


class HashSetTest(unittest.TestCase):
    """Test Set implemented using a HashTable."""

    def test_init(self):
        """Initialize Set and check to see if default values are set."""
        st = Set(4)
        assert len(st.buckets) == 4
        assert st.length() == 0
        assert st.size == 0

    def test_elements(self):
        """Check if a list of items in the Set can be retrieved."""
        st = Set()
        assert st.elements() == []
        st.add('A')
        assert st.elements() == ['A']
        st.add('tiny')
        self.assertCountEqual(st.elements(), ['A', 'tiny'])
        st.add('set')
        self.assertCountEqual(st.elements(), ['A', 'tiny', 'set'])

    def test_length(self):
        """Check if the length is updated properly."""
        st = Set()
        assert st.length() == 0
        st.add('check')
        assert st.length() == 1
        st.add('set')
        assert st.length() == 2
        st.add('size')
        assert st.length() == 3

    def test_contains(self):
        """Check to see if the contains method works as intended."""
        st = Set()
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
        """Check to see if items can be removed from the Set."""
        st = Set()
        st.add('Please')
        st.add('dont')
        st.add('remove')
        st.add('me')
        assert st.length() == 4
        st.remove('please')
        st.remove('dont')
        assert st.length() == 2
        self.assertCountEqual(st.elements(), ['remove', 'me'])
        st.remove('me')
        st.length() == 1
        with self.assertRaises(KeyError):
            st.delete('NOOOO')

    def test_union(self):
        """Check if the union operation works as intended."""
        pass

    def test_intersection(self):
        """Check if the intersection operation works as intended."""
        pass

    def test_difference(self):
        """Check if the difference operation works as intended."""
        pass
