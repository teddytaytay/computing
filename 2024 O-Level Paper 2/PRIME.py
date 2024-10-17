def div_2(number):
    halved = int(number / 2)
    return halved

def odd_or_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

def prime(number):
    if number <= 1:
        return "Not prime"
    if number == 2:
        return "Prime"
    if number % 2 == 0:
        return "Not prime"
    half = div_2(number)
    for i in range(3, half+1):
        if number % i == 0:
            return "Not prime"
    return "Prime"

number = int(input("Enter a whole number: "))
print(prime(number))