def word_count(a):
    return len(a.split())


string = str(input("Enter the string: "))
print(word_count(string))