data = [("a", 1), ("b", 2), ("c", 3)]

result = {}

for item in data:
    key = item[0]
    value = item[1]
    result[key] = value

print("Dictionary:", result)
