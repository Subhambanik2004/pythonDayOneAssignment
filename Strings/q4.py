text = input("Enter a string: ")
frequency = {}
for ch in text:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1
for key in frequency:
    print(key, ":", frequency[key])
