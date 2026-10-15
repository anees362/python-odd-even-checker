try:
    a = int(input("Type your number to check if its odd or even: "))

    if a % 2 == 0:
        print("its an even number")

    else:
        print("its an odd number")

except ValueError:
    print("You can only type numbers!")
