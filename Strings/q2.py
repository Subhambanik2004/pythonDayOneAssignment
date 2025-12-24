text = input("Enter your text : ")
words = text.split()

res = ""
for word in words:

    res = res + word[::-1] + " "
print(res)
