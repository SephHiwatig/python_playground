'''
This program generates fibbonacci sequence to the nth number
'''

while True:
    try:
        user_input = int(input("Please enter the number of fibonacci numbers you want to generate"))
    except:
        print("Please enter a valid number")
    else:
        break

a = 0
b = 1 
fibonaccis = []
for i in range(user_input):
    fibonaccis.append(a)
    temp = a
    a = b
    b = temp + b

print(fibonaccis)
