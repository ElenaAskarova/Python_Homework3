# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 6

# -> 5

n = int(input('Введите количество элементов в массиве: '))
x = int(input('Введите число Х: '))
list1 = []

for i in range(n):
    list1.append(i)
print(*list1)
    
result = list1[0]
if abs(i - x) < abs(result - x):
    result = i   
    
print(result)


