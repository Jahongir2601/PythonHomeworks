def check(func):
    def wrapper(x, y):
        if y == 0:
            print('Denominator cannot be zero')
            return None  
        return func(x, y)
    return wrapper

@check
def div(x, y):
    return x / y

def main():
    while True:
        try:
            x = float(input('Enter the first number: '))
        except ValueError:
            print('Enter a real number')
            continue
        try:
            y = float(input('Enter the second number: '))
        except ValueError:
            print('Enter a real number')
            continue
        
        result = div(x, y)
        if result is not None:
            print(f'{x} / {y} = {result}')

if __name__ == "__main__":
    main()