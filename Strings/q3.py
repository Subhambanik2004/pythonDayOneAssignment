text = input("Enter your text : ")

reverse_text = text[::-1]

if text == reverse_text:
    print("the word is an palindrome")
else:
    print("the word is not an palindrome")
