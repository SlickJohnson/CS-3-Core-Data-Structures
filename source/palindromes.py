#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    return is_palindrome_recursive(text)
    # return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    """Check if provided text is a palindrome iteratively.

    Args:
        text: str -- the string that will be checked for palindromness.

    Returns: bool -- results of palindrome check.

    """
    # ignore case, punctuation, and whitespace.
    translator = str.maketrans("", "", string.punctuation)
    text = text.lower().translate(translator).replace(" ", "")

    # Only one character so it's a palindrome.
    if len(text) <= 1:
        return True

    # rearange character order.
    palindrome = []
    for char in text:
        palindrome.insert(0, char)

    return "".join(palindrome) == text


def is_palindrome_recursive(text, left=None, right=None):
    """Check if provided text is a palindrome recusrsively.

    Args:
        text: str -- the string that will be checked for palindromness.
        left: list -- holds the left side of text.
        right: list -- holds the right side of text.

    Returns: bool -- results of palindrome check.

    """
    # ignore case, punctuation, and whitespace.
    translator = str.maketrans("", "", string.punctuation)
    text = text.lower().translate(translator).replace(" ", "")

    # Only one character so it's a palindrome.
    if len(text) <= 1:
        return True

    # First iteration.
    if not left or not right:
        return is_palindrome_recursive(text, [text[0]], [text[-1]])

    left_index = len(left)
    right_index = -1 * len(right) - 1

    # Test for symmetry.
    if not "".join(left) == "".join(right):
        return False
    # Base case.
    elif len(left) + len(right) >= len(text):
        return True
    else:
        left.append(text[left_index])
        right.append(text[right_index])
        return is_palindrome_recursive(text, left, right)


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
