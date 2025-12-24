text = "Subham"
try:
    text[1] = "a"

except TypeError as e:
    print("Error :", e)

print("Original string:", text)
