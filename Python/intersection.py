def intersection(set1, set2):
  """
  Calculates the intersection of two sets.

  Args:
      set1: The first set.
      set2: The second set.

  Returns:
      A new set containing elements present in both sets.
  """
  return set1 & set2

# Example usage
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
intersection_set = intersection(set1, set2)
print(intersection_set)  # Output: {3, 4}
