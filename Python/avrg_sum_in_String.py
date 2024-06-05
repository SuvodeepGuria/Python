def sum_and_average_characters(string):
  """
  Calculates the sum and average of ASCII values of characters in a string.

  Args:
      string: The input string.

  Returns:
      A tuple containing the sum and average of ASCII values.
  """
  sum_ascii = 0
  for char in string:
    if char.isalpha():
      sum_ascii += ord(char)  # Get ASCII value
  if not sum_ascii:
    return (0, 0)  # Handle empty string or non-alphabetic characters
  return (sum_ascii, sum_ascii / len(string))

# Example usage
string = "Apple"
sum_avg = sum_and_average_characters(string)
print(sum_avg)  # Output: (603, 120.6)
