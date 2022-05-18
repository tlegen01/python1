import math
def calk(number1, operation, number2 = 10,):
    print(number1, number2, operation)
    if operation == "+":
        return number1 + number2
    if operation == "-":
        return number1 - number2
    if operation == "*":
        return number1 * number2
    if operation == "/":
        if number1 != 0:
            return number1 / number2
        else:
            print("vy vveli 0")
            return 0
    if operation == "**":  # vozvedenie v stepen
        return number1 ** number2
    if operation == "//":  # Delenie bez ostatka
        return number1 // number2
    if operation == "%":
        return number1 % number2
    if operation == "///":
        return math.sqrt(number1)



result = calk(9, "/",)
print(result)



