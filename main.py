def factOrSum(x, o):
    if o == "factorial":
        number = 1
        for i in range (1, x + 1):
            number = number * i
        return number
    else:
        number = 0
        for i in range (1, x + 1):
            number = number + i
        return number

print(factOrSum(4, "factorial"))
print(factOrSum(10, "sum"))