import math

# This project will prompt user to enter how many decimals
# will appear after e

while True:
    try:
        user_input = int(input("Please enter how many decimals should appear for e (1 - 20)"))
    except:
        print("Please enter a valid number.")
    else:
        if user_input in list(range(1, 21)):
            break
        else:
            print("Please enter a valid number.")

print("e is:")
print(round(math.e, user_input))