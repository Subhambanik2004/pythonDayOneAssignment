tuple = (1, 2, 3, 4, 2, 3, 1, 1, 2, 4, 2, 3, 1, 2, 3, 4, 2)
freq = {}

for ele in tuple:
    if ele in freq:
        freq[ele] += 1
    else:
        freq[ele] = 1

for key in freq:
    print(key, " : ", freq[key])
