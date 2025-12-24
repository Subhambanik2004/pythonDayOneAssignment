vowels = 0
consonents = 0
digits = 0
special = 0

text = input("Enter whatever you want : ")
for ch in text:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonents += 1
    elif ch.isdigit():
        digits += 1
    else:
        special += 1

print("Vowels :", vowels)
print("Consonents :", consonents)
print("Digits :", digits)
print("Special :", special)
