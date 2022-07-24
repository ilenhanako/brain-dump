#NOT finished

def prime_checker(number):
    number %= 2
    if number == 0:
        number %= 1
        if number == 0:
            print("It's a prime number.")
    else:
        print("It's not a prime number.")



n = int(input("Check this number: "))
prime_checker(number=n)