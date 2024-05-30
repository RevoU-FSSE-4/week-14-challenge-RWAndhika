# anagram.py

def is_anagram(s1: str, s2: str) -> bool:
    """
    This function checks if the two given strings `s1` and `s2` are anagrams.
    
    Two strings are anagrams if they contain the same characters with the same frequencies,
    ignoring spaces and capitalization.
    
    Args:
    - s1 (str): The first input string.
    - s2 (str): The second input string.
    
    Returns:
    - bool: True if the strings are anagrams, False otherwise.
    
    Examples:
    - is_anagram("Listen", "Silent") should return True
    - is_anagram("hello", "billion") should return False
    """
    # Step 1: Clean the strings by removing non-alphanumeric characters and converting to lowercase
    # Step 2: Compare the character counts of both cleaned strings
    
    # Implement your solution here
    s1_length = 0
    s1_temp_list = []
    s2_length = 0
    s2_temp_list = []
    for char in s1.lower():
        if "a" <= char <= "z":
            s1_temp_list = s1_temp_list + [char]
            s1_length += 1
    
    for char in s2.lower():
        if "a" <= char <= "z":
            s2_temp_list = s2_temp_list + [char]
            s2_length += 1

    if s1_length == s2_length:
        temp_dict1 = {}
        temp_dict2 = {}
        for char in s1_temp_list:
            if char in temp_dict1:
                temp_dict1[char] += 1
            else:
                temp_dict1[char] = 1
        
        for char in s2_temp_list:
            if char in temp_dict2:
                temp_dict2[char] += 1
            else:
                temp_dict2[char] = 1
        
        if temp_dict1 == temp_dict2:
            return True
        else:
            return False
    else:
        return False

# You can test your function with print statements below
# Example:
# print(is_anagram("Listen", "Silent"))  # Expected output: True
# print(is_anagram("hello", "billion"))  # Expected output: False
