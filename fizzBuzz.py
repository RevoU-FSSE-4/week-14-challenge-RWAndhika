# fizzbuzz.py

def fizzbuzz(n: int) -> list:
    """
    This function returns a list of strings with the numbers from 1 to `n`.
    But for multiples of three, return "Fizz" instead of the number and for the multiples of five, return "Buzz".
    For numbers which are multiples of both three and five, return "FizzBuzz".

    Args:
    - n (int): The upper limit of the range (inclusive).

    Returns:
    - list: A list of strings representing the FizzBuzz sequence.
    
    Examples:
    - fizzbuzz(15) should return ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]
    """
    # Implement your solution here
    result = []
    for number in range(1, n + 1):
        if number % 3 == 0 and number % 5 == 0:
            result = result + ["FizzBuzz"]
        elif number % 3 == 0:
            result = result + ["Fizz"]
        elif number % 5 == 0:
            result = result + ["Buzz"]
        else:
            result = result + [str(number)]
    return result

# You can test your function with print statements below
# Example:
# print(fizzbuzz(15))  # Expected output: ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]
