list = [1, 2, 3, 4, 2, 1, 3, 1, 4, 2, 1, 4, 3, 4, 2, 2, 1]
unique_list = []

for ele in list:
    if ele in unique_list:
        continue
    else:
        unique_list.append(ele)

print(unique_list)
