a = input("Enter a sentence: ")
b = a.split()
c = ''
for word in b:
    c += word[0]
print(c.upper())
