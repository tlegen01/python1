def calk(number1, number2, operation):
    print(number1, number2, operation)
    if operation == "+":
        return number1 + number2
    if operation == "-":
        return number1 - number2


result = calk(10, 3, "-")
print(result)

result = calk(-11, -5, "-")
print(result)
