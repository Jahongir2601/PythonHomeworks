# 1
def celcius_to_far(x:float):
    return 1.8*x + 32
def far_to_celcius(x:float):
    return (x-32)*5/9

while True:
    try:
        a = float(input('Enter a temperature in degrees F: '))
        print(f'{a} degrees F = {far_to_celcius(a):.2f} degrees C')
        b = float(input('Enter a temperature in degrees C: '))
        print(f'{b} degrees C = {celcius_to_far(b):.2f} degrees F')
        break
    except:
        print('Enter a real number')