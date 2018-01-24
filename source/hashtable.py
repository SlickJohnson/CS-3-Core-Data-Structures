#!python
"""Implementation of HashTable."""
from linkedlist import LinkedList


class HashTable(object):
    """HashTable object that holds data that can be quickly retrieved.

    Attributes:
        buckets: A list of LinkedLists that will hold the data

    """

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        self.buckets = [LinkedList() for i in range(init_size)]
        self.size = 0  # Number of key-value entries

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        return hash(key) % len(self.buckets)

    def load_factor(self):
        """Return the load factor, the ratio of number of entries to buckets.

        Performance:
            Best/Worst: O(1), quick maths.
        """
        return self.size / len(self.buckets)  # O(1)

    def keys(self):
        """Return a list of all keys in this hash table.

        Performance:
            Best/Worst: O(n), because it has to loop through the all the all
                entries in the hashtable.
        """
        # Collect all keys in each of the buckets
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.

        Performance:
            Best/Worst: O(n), because it has to loop through all the entries in
                the hashtable.
        """
        # Collect all values in each of the buckets
        all_values = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_values.append(value)
        return all_values

    def items(self):
        """Return a list of all key-value pairs in this hash table.

        Performance:
            Best and worse case O(n), because it has to loop through all the
                buckets in the HashTable
        """
        # Collect all pairs of key-value entries in each of the buckets
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.

        Performance:
            Best/Worst: O(1), accessing variables is an O(n) operation.
        """
        return self.size

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.

        Performance:
            Best: O(1), if the item key is the first in the hashtable.
            Worst: O(n), if the key is not in the hashtable.
        """
        # Find the bucket the given key belongs in
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # Check if an entry with the given key exists in that bucket
        entry = bucket.find(lambda key_value: key_value[0] == key)
        return entry is not None  # True or False

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.

        Performance:
            Best: O(1), if key is in the first position of the first bucket
            Worst: O(n^2), if key is at the very end of the HashTable
        """
        # Find the bucket the given key belongs in
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # Find the entry with the given key in that bucket, if one exists
        entry = bucket.find(lambda key_value: key_value[0] == key)
        if entry is not None:  # Found
            # Return the given key's associated value
            assert isinstance(entry, tuple)
            assert len(entry) == 2
            return entry[1]
        else:  # Not found
            raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value.

        Performance:
            Best/Worst: O(n), checks if the key-value is alredy in the
                hashtable which is an O(n) operation.
        """
        # Find the bucket the given key belongs in
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # Find the entry with the given key in that bucket, if one exists
        # Check if an entry with the given key exists in that bucket
        entry = bucket.find(lambda key_value: key_value[0] == key)
        if entry is not None:  # Found
            # In this case, the given key's value is being updated
            # Remove the old key-value entry from the bucket first
            self.delete(key)  # O(n)
        # Insert the new key-value entry into the bucket in either case
        bucket.append((key, value))  # O(1)
        self.size += 1  # O(1)

        # Check if the load factor exceeds 0.75
        if self.load_factor() > 0.75:  # O(1)
            self._resize()  # O(n)

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.

        Args:
            key: any -- key of the entry to be deleted.
        Performance:
            Best: O(1), if the key is the first in the HashTable
            Worst: O(n), if key is at the very end of the bucket, or if the key
                is not found.

        Raises:
            KeyError: If key not found in the hashtable.

        """
        # Find the bucket the given key belongs in
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # Find the entry with the given key in that bucket, if one exists
        entry = bucket.find(lambda key_value: key_value[0] == key)
        if entry is not None:  # Found
            # Remove the key-value entry from the bucket
            bucket.delete(entry)
            self.size -= 1
            print(key, self.size)
        else:  # Not found
            raise KeyError('Key not found: {}'.format(key))

    def _resize(self, new_size=None):
        """Resize this hash table's buckets and rehash all key-value entries.

        Args:
            new_size: int -- The size the hashtable should expand/shrink to.

        Performance:
            Best/Worst: O(n), because it has to loop through all items in the
                hashtable to update their position in the hashtable.

        """
        # If unspecified, choose new size dynamically based on current size
        if new_size is None:  # O(1)
            new_size = len(self.buckets) * 2  # O(1), double size
        # Reduce size if buckets are sparsely filled (low load factor)
        elif new_size is 0:  # O(1)
            new_size = len(self.buckets) / 2  # O(1), half size

        entries = self.items()  # O(n), get all items.
        # O(n), create empty buckets.
        self.buckets = [LinkedList() for i in range(new_size)]
        self.size = 0  # O(1), reset size.
        for key, value in enumerate(entries):  # O(n), put entries in new list.
            self.set(key, value)


def test_hash_table():
    ht = HashTable(4)
    print('HashTable: ' + str(ht))

    print('Setting entries:')
    ht.set('I', 1)
    print('set(I, 1): ' + str(ht))
    ht.set('V', 5)
    print('set(V, 5): ' + str(ht))
    print('size: ' + str(ht.size))
    print('length: ' + str(ht.length()))
    print('buckets: ' + str(len(ht.buckets)))
    print('load_factor: ' + str(ht.load_factor()))
    ht.set('X', 10)
    print('set(X, 10): ' + str(ht))
    ht.set('L', 50)  # Should trigger resize
    print('set(L, 50): ' + str(ht))
    print('size: ' + str(ht.size))
    print('length: ' + str(ht.length()))
    print('buckets: ' + str(len(ht.buckets)))
    print('load_factor: ' + str(ht.load_factor()))

    print('Getting entries:')
    print('get(I): ' + str(ht.get('I')))
    print('get(V): ' + str(ht.get('V')))
    print('get(X): ' + str(ht.get('X')))
    print('get(L): ' + str(ht.get('L')))
    print('contains(X): ' + str(ht.contains('X')))
    print('contains(Z): ' + str(ht.contains('Z')))

    print('Deleting entries:')
    ht.delete('I')
    print('delete(I): ' + str(ht))
    ht.delete('V')
    print('delete(V): ' + str(ht))
    ht.delete('X')
    print('delete(X): ' + str(ht))
    ht.delete('L')
    print('delete(L): ' + str(ht))
    print('contains(X): ' + str(ht.contains('X')))
    print('size: ' + str(ht.size))
    print('length: ' + str(ht.length()))
    print('buckets: ' + str(len(ht.buckets)))
    print('load_factor: ' + str(ht.load_factor()))


if __name__ == '__main__':
    test_hash_table()
