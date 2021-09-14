from random import randint


def maximum(*args):
    return max(*args)


numbers = [randint(1, 100) for i in range(1, 10)]
print(maximum(numbers))