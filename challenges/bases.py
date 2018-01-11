#!python
"""Base conversion."""
import string


def decode(digits, base):
    """Decode given digits in given base to number in base 10.

    Args:
        digits: str -- string representation of number (in given base)
        base: int -- base of given number

    Returns: int -- integer representation of number (in base 10)

    """
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)

    # all characters that will be used for base conversion.
    possible_chars = string.digits + string.ascii_lowercase

    result = 0
    for exponent in range(0, len(digits)):
        index = len(digits) - exponent - 1
        digit = digits[index]
        power = base ** exponent

        digit = possible_chars.index(digit.lower())

        value = digit * power
        result += value

    return result


def encode(number, base):
    """Encode given number in base 10 to digits in given base.

    Args:
        number: int -- integer representation of number (in base 10)
        base: int -- base to convert to

    Returns: str -- string representation of number (in given base)

    """
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)

    # all characters that will be used for base conversion.
    possible_chars = string.digits + string.ascii_lowercase

    quotient = number
    answer = ""

    while quotient != 0:
        remainder = quotient % base
        answer = "{}{}".format(possible_chars[remainder], answer)
        quotient = int(quotient / base)

    return answer


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.

    Args:
        digits: str -- string representation of number (in base1)
        base1: int -- base of given number
        base2: int -- base to convert to

    Returns: str -- string representation of number (in base2)

    """
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)

    return encode(decode(digits, base1), base2)


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name

    digits = args[0]
    base1 = int(args[1])

    if len(args) == 3:
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')
        print(decode(digits, base1))


if __name__ == '__main__':
    # main()
    import sys
    args = sys.argv[1:]

    print(decode(str(args[0]), int(args[1])))
