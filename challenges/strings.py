#!python


def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    if pattern == '':
        return True

    match = ''  # Pattern chain.
    patt_index = 0
    for text_char in text:
        patt_char = pattern[patt_index]

        if text_char == patt_char:
            # Continue chain.
            match += text_char
            patt_index += 1
        else:
            # Break chain.
            patt_index = 0
            match = ''

            # Check if char that broke chain matches first char in pattern.
            if text_char == pattern[0]:
                match += text_char
                patt_index += 1

        if match == pattern:
            return True

    return False


def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    if pattern == '':
        return 0

    match = ''  # Pattern chain.
    patt_index = 0
    for index, text_char in enumerate(text):
        patt_char = pattern[patt_index]

        if text_char == patt_char:
            # Continue chain.
            match += text_char
            patt_index += 1
        else:
            # Break chain.
            patt_index = 0
            match = ''

            # Check if char that broke chain matches first char in pattern.
            if text_char == pattern[0]:
                match += text_char
                patt_index += 1

        if match == pattern:
            return index - len(pattern) + 1

    return None


def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)


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
