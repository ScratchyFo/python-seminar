#За день машина проезжает n километров. Сколько
#дней нужно, чтобы проехать маршрут длиной m
#километров? При решении этой задачи нельзя
#пользоваться условной инструкцией if и циклами.
#Input:
#n = 700
#m = 750
#Output:
#2

print("Введите количество километров за день: ")
n = int(input())

print("Введите длину пути, км:")

m = int(input())
c = int((m / n) + 0.9999)
#c = m / n
print(f"Понадобится ехать в течение {c} дней")