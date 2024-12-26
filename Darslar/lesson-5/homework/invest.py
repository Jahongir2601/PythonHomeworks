# 2 
def invest(amount:float, rate:float, years:int):
    for i in range(1,years+1):
        money = amount * pow(1+rate,i)
        print(f'year {i}: ${money:.2f}')
a = float(input("Enter an initial amount: "))
b = float(input("Enter an annual percentage rate: "))
c = int(input("Enter number of years: "))
invest(a, b, c)