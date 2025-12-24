import copy

original = [[1, 2], [3, 4]]
shallow_copy = original.copy()
deep_copy = copy.deepcopy(original)
original[0][0] = 99
print("Original:", original)
print("Shallow Copy:", shallow_copy)
print("Deep Copy:", deep_copy)
