a = input()
b = int('0' in a)
c = int('1' in a)
d = int('2' in a)
e = int('3' in a)
f = int('4' in a)
g = int('5' in a)
h = int('6' in a)
i = int('7' in a)
j = int('8' in a)
k = int('9' in a)
f = b+c+d+e+f+g+h+i+j+k

if f == 0:
    print("String doesn't contain digit")
else:
    print('String contains digit')