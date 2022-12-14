n = int(input("Введите число: "))
lst = [i for i in range(-n, n + 1)]

print(lst)
text = input("Введите индексы: ")
index = []
index = text.split(" ")

def swr(text):
    result = 1
    for item in text:
        if item.isdigit():
            ind = int(item)
            if ind in range(0, len(lst)):
                result = result * lst[ind]
            else:
                return "Вы вышли за пределы массива"
    return result

print(swr(index))