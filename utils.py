def is_palindrome(s):
    """Check whether a string is a palindrome."""
    return s == s[::-1]


def count_words(text):
    """Count the number of words in a text string."""
    return len(text.split())


def celsius_to_fahrenheit(c):
    """Convert temperature from Celsius to Fahrenheit."""
    return (c * 9 / 5) + 32


# Test cases
print("Is 'racecar' a palindrome?:", is_palindrome("racecar"))
print("Word count:", count_words("Hello AI Tools Lab"))
print("25°C in Fahrenheit:", celsius_to_fahrenheit(25))
