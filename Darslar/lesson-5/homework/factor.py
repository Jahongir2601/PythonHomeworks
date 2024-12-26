def factor(n:int):
    for i in range(1,int(1+n)):
        if n % i == 0:
            print(f'{i} is a factor of {n}')
a = int(input("Enter a positive integer: "))
factor(a)