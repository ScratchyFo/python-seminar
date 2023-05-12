#Задача 26:  Посчитать факториал (произведение 1 до N) и треугольное число
# (сумма чисел от 1 до N) для числа N ЧЕРЕЗ РЕКУРСИЮ и без циклов

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
def triangular(n):
    if n == 1:
        return 1
    else:
        return n + triangular(n-1)
    

print('Введите N число: ')
n = int(input())

print(factorial(n))
print(triangular(n))
