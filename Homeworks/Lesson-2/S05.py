string = "Hello World"
vowels = 'aeiou'
vovel_num = 0 
cons_num = 0

for x in string.lower():
    if x.isalpha():
        if x in vowels:
            vovel_num = vovel_num + 1
        else:
            cons_num = cons_num + 1

print("Number of vowels:", vovel_num)
print('Number of consonants:', cons_num)

