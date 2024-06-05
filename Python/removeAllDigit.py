def remove_digits(string):
  """
  Removes all digits from a string.

  Args:
      string: The input string.

  Returns:
      A new string with digits removed.
  """
  return ''.join(char for char in string if not char.isdigit())

# Example usage
string = "Hello123World"
digit_free_string = remove_digits(string)
print(digit_free_string)  # Output: HelloWorld
