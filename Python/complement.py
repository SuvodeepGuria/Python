def complement(universal_set, set1):
  """
  Finds the complement of a set within a universal set (elements in the universal set but not in set1).

  Args:
      universal_set: The set representing the entire domain.
      set1: The set whose complement is to be found.

  Returns:
      A new set containing elements in the universal set but not in set1.
  """
  return universal_set - set1

# Example usage
universal_set = {1, 2, 3, 4, 5, 6, 7, 8}
set1 = {3, 4, 5, 6}
complement_set = complement(universal_set, set1)
print(complement_set)  # Output: {1, 2, 7, 8}
