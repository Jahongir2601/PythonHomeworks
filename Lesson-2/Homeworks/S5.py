def count(string):
    vowels = 'aeiou'
    vovel_num = 0 
    cons_num = 0

    for char in string.lower():
        if char.isalpha():
            if char in vowels:
                vovel_num = vovel_num + 1
            else:
                cons_num = cons_num + 1
    return vovel_num, cons_num

a = "Hello World"
x, y = count(a)
print("Number of vowels:", x)
print('Number of consonants:', y)

