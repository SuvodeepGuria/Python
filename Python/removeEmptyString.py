def remove_empty_strings(string_list):
  """
  Removes empty strings from a list of strings.

  Args:
      string_list: A list of strings.

  Returns:
      A new list with empty strings removed.
  """
  return [string for string in string_list if string]

# Example usage
string_list = ["Hello", "", "World", "", "Python"]
filtered_list = remove_empty_strings(string_list)
print(filtered_list)  # Output: ['Hello', 'World', 'Python']
