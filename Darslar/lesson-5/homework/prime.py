def prime_check(a):
    if a < 2:
        return False
    for i in range(2,int(pow(a, 0.5)+1)):
        if a % i == 0:
            return False
    return True

n = int(input('Enter an integer: '))
print(prime_check(n))