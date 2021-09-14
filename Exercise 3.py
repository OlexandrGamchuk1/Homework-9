def rectangle(length, width):
    for i in range(length):
        for j in range(width):
            print("*", end="")
        print()


number = int(input("Enter the length: "))
number1 = int(input("Enter the width: "))
rectangle(number, number1)