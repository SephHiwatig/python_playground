import math

# This project will prompt user to enter how many decimals
# will appear after PI

while True:
    try:
        user_input = int(input("Please enter how many decimals should appear for PI (1 - 20)"))
    except:
        print("Please enter a valid number.")
    else:
        if user_input in list(range(1, 21)):
            break
        else:
            print("Please enter a valid number.")

print("PI is:")
print(round(math.pi, user_input))