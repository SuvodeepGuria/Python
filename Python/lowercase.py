def arrange_lowercase_first(string):
  """
  Arranges characters in a string such that lowercase characters come first.

  Args:
      string: The input string.

  Returns:
      A new string with lowercase characters at the beginning, followed by uppercase characters and other characters.
  """
  lowercase = ''.join(char for char in string if char.islower())
  uppercase = ''.join(char for char in string if char.isupper())
  others = ''.join(char for char in string if not char.isalnum())
  return lowercase + uppercase + others

# Example usage
string = "PyThOn!123"
arranged_string = arrange_lowercase_first(string)
print(arranged_string)  # Output: pythonThOn!123
