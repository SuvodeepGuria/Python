def difference(set1, set2):
  """
  Calculates the difference between two sets (elements in set1 but not in set2).

  Args:
      set1: The first set.
      set2: The second set.

  Returns:
      A new set containing elements in set1 but not in set2.
  """
  return set1 - set2

# Example usage
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
difference_set = difference(set1, set2)
print(difference_set)  # Output: {1, 2}
