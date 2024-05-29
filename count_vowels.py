# count_vowels.py


def count_vowels(s: str) -> int:
    """
    This function counts the number of vowels (a, e, i, o, u) in a given string `s`.

    Args:
    - s (str): The input string.

    Returns:
    - int: The number of vowels in the string.

    Examples:
    - count_vowels("hello world") should return 3
    - count_vowels("python") should return 1
    """
    # Implement your solution here
    result = 0
    for char in s:
        if (
            char == "a"
            or char == "e"
            or char == "i"
            or char == "o"
            or char == "u"
            or char == "A"
            or char == "E"
            or char == "I"
            or char == "O"
            or char == "U"
        ):
            result += 1

    return result

# You can test your function with print statements below
# Example:
# print(count_vowels("hello world"))  # Expected output: 3
# print(count_vowels("python"))  # Expected output: 1
