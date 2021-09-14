def palindrome():
    my_list = []
    my_dictionary = {}
    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            a = str(i * j)
            if a == a[::-1]:
                my_dictionary[i * j] = f"{i} * {j}"
                my_list.append(i * j)
    maximum = max(my_list)
    print(f"{maximum} = {my_dictionary.pop(maximum)}")


palindrome()