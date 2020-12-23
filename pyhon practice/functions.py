# built in functions

# a = 99
# b = 88
# c = sum((a, b))
# print(c)

# user defined functions

# def function1():
#     print("Hello world I am fUNCTION 1")
# print(function1())

a = int(input())
b = int(input())


def function2(a, b):
    """This is a program which calculate average of two numbers
    this is called docstrings of function2"""
    average = (a+b)/2
    print(average)
    return average


print(function2(a, b))

#method to print docstring
print(function2.__doc__)
