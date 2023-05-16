indexs = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min = 5
max = 15
indelem = []

for i in range(len(indexs)):
    if min <= indexs[i] <= max:
        indelem.append(i)

print(indelem)