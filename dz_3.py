tuple1 = (1, 2, 3, 4, 5)
tuple2 = (2, 3, 6, 4, 7)
tuple3 = (2, 8, 3, 4, 9)

result = []

for i in range(min(len(tuple1), len(tuple2), len(tuple3))):
    if tuple1[i] == tuple2[i] == tuple3[i]:
        result.append(tuple1[i])

print(result)