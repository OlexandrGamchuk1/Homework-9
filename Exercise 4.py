def linear_search(a, b):
    if b in a:
        return my_list.index(b)
    return -1


my_list = [i for i in range(1, 100)]
number = int(input("Enter the number: "))
print(linear_search(my_list, number))