# Program to perform different operations on a string
text = input("Enter a string: ")

print("a. Original string:", text)
print("b. Length:", len(text))
print("c. First character:", text[0])
print("c. Last character:", text[-1])
print("d. Reverse order:", text[::-1])
print("e. Substring (index 2 to 6):", text[2:7])
print("f. Uppercase:", text.upper())
print("g. Lowercase:", text.lower())

ch = input("Enter a character to count: ")
print("h. Occurrences of", ch, "=", text.count(ch))

old = input("Enter the word to be replaced: ")
new = input("Enter new word: ")
print("i. After replacing:", text.replace(old, new))

print("j. After removing spaces:", text.strip())