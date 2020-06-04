'''
This program finds all the prime factors of a given user input
'''
import math

def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True

    root = int(math.sqrt(num))
    for x in range(3, root + 1, 2):
        if num % x == 0:
            return False
    return True

while True:
    try:
        user_input = int(input("Please enter a positive number to factor"))
    except:
        print("Please enter a valid number")
    else:
        if user_input == 1:
            print("1 is neither prime nor composite")
            continue
        if user_input < 1:
            print("Please use positive non-zero integers")
            continue
        if is_prime(user_input):
            print(f'{user_input} is a prime number')
            continue
        break

print("Composite number entered")
