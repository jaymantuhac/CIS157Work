#Chapter 7 Exercise 12
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


print(is_leap_year(2019)) #Expect False, not divisible by 3
print(is_leap_year(2000)) #Expect True, divisible by 100 and 400
print(is_leap_year(2100)) #Expect False, divisible by 100, but not 400

#Chapter 7 Exercise 13
def date_formatting(date):
    if date > 31:
        print("April", date - 31)
    else:
        print("March", date)

def easter_calculator():
    year = int(input("Enter a year between 1900 and 2099:"))
    a = year % 19
    b = year % 4
    c = year % 7
    d = (19 * a + 24) % 30
    e = (2 * b + 4 * c + 6 * d + 5) % 7
    dateofeaster = 22 + d + e

    if year > 1899 and year < 3000:
        if year in (1954, 1981, 2049, 2076):
            dateofeaster -= 7
            return date_formatting(dateofeaster)
        else:
            return date_formatting(dateofeaster)
    else:
        print("This year is out of range. Try again.")

easter_calculator()

#Chapter 8 Exercise 1
def newtonSqrt(n, howmany):
    approx = 0.5 * n
    for i in range(howmany):
        betterapprox = 0.5 * (approx + n/approx)
        approx = betterapprox
        print('better')
    return betterapprox

print(newtonSqrt(25,4))

#Chapter 8 Exercise 2
def print_triangular_numbers(n):
    adding = 0
    number = 0
    iteration = 0
    for i in range(n):
        iteration += 1
        adding += 1
        number += adding
        print(iteration, number)

print_triangular_numbers(5)
