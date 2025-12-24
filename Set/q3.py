set1 = {1, 2, 3, 4}
set2 = {3, 4}

is_subset = set2.issubset(set1)

if is_subset:
    print("set2 is a subset of set1")
else:
    print("set2 is not a subset of set1")
