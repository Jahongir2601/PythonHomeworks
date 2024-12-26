universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]
def enrollment_stats(university):
    enrollments = []
    fees = []
    for i in university:
        enrollments.append(i[1])
        fees.append(i[2])
    return enrollments, fees
def mean(numbers):
    return sum(numbers)/len(numbers)
def median(numbers):
    if len(numbers) % 2 == 1:
        a = sorted(numbers)[int((len(numbers)+1)/2-1)]
    else:
        a = 0.5 * sorted(numbers)[len(numbers)/2-1] + 0.5 * sorted(numbers)[len(numbers)/2]
    return a
def main():
    enrollments, fees = enrollment_stats(universities)
    print('*'*20)
    print('Total students:', sum(enrollments))
    print('Total tuition: $', sum(fees))

    print(f'Student mean: {mean(enrollments):.2f}')
    print('Student median:', median(enrollments))
    
    print(f'Tuition mean: $ {mean(fees):.2f}')
    print('Tuition median: $', median(fees))
    print('*'*20)

main()