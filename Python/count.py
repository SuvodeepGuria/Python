def count_characters(string):
  """
  Counts the total number of characters, digits, and special symbols in a string.

  Args:
      string: The input string.

  Returns:
      A dictionary containing counts for characters, digits, and special symbols.
  """
  char_count = 0
  digit_count = 0
  special_count = 0
  for char in string:
    if char.isalpha():
      char_count += 1
    elif char.isdigit():
      digit_count += 1
    else:
      special_count += 1
  return {'characters': char_count, 'digits': digit_count, 'special_symbols': special_count}

# Example usage
string = "Hello, World123!"
counts = count_characters(string)
print(counts)  # Output: {'characters': 11, 'digits': 3, 'special_symbols': 2}
