a = input('Enter the sentence: ')
b = a.split()
c = b[0]
d = b[-1]
if c == 'Python' and d == 'fun!':
    print(True)
else:
    print(False)