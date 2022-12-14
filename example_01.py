n = int(input("Введите число: "))
result = 0
lst = [(lambda x: round((1 + 1/x)**x, 3))(i) for i in range(1, n + 1)]
for item in lst:
    result = result + item
print(lst, end=" = ")
print(result)