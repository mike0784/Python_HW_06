import random as rnd
n = int(input("Введите диапазон массива: "))
arr = [rnd.randint(-100, 100) for i in range(0, n + 1)]
print(arr)

def mixing():
    n1 = rnd. randint(0, n)
    n2 = rnd. randint(0, n)
    temp = arr[n1]
    arr[n1] = arr[n2]
    arr[n2] = temp

for i in range(0, n + 1):
    mixing()
print(arr)