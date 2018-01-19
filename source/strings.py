#!python
"""String searching algorithms."""


def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    # Returns true of there is an index found
    return find_index(text, pattern) is not None


def find_index(text, pattern, offset=0):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    if pattern == '':
        return 0

    patt_index = 0
    matches = 0
    for text_index in range(offset, len(text)):
        for patt_index in range(len(pattern)):
            # Prevent index out of range errors.
            if text_index + patt_index >= len(text):
                break

            # Break loop if there's a char mismatch.
            if text[text_index + patt_index] != pattern[patt_index]:
                matches = 0
                break

            matches += 1

        if matches == len(pattern):
            return text_index

    return None


def find_all_indexes(text, pattern, indexes=None, offset=None):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    if pattern == '':
        return [index for index, _ in enumerate(text)]

    if indexes is None or offset is None:
        indexes = []
        offset = 0

    # Find pattern index starting from given offset.
    found_index = find_index(text, pattern, offset)

    # Base case. If no pattern found, end recursive cycle.
    if found_index is None:
        return indexes

    indexes.append(found_index)

    # Skip unnecessary characters
    offset = found_index + len(pattern)
    # But account for overlapping patterns.
    if len(pattern) > 1:
        offset -= 1

    return find_all_indexes(text, pattern, indexes, offset)


def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()
