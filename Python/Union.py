def union(set1, set2):
  """
  Performs the union of two sets.

  Args:
      set1: The first set.
      set2: The second set.

  Returns:
      A new set containing elements from both sets.
  """
  return set1 | set2

# Example usage
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
union_set = union(set1, set2)
print(union_set)  # Output: {1, 2, 3, 4, 5, 6}
