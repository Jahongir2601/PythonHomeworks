a = input('Enter a string: ')
b = 'aoeiu'
result = ''
for x in a:
    if x in b:
        result += '*'
    else:
        result += x
print(result)