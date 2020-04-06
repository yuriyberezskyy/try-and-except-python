def divides(a, b):
    try:
        result = a/b
        print(result)
    except ZeroDivisionError:
        print("Can't divide by zero")


print(divides(1, 0))
print(divides(12, 6))
