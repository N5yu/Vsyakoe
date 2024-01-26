import random
a = [[random.randint(-30, 30) for _ in range (3)],[random.randint(-30, 30) for _ in range (3)], [random.randint(-30, 30) for _ in range (3)]]
max_value = int(-1)
min_value = int(1)
total_sum = 0
total_el = 0
for row in a:
    for element in row:

        if element > max_value:
            max_value = element
        elif element < min_value:
            min_value = element
        total_sum += element
        total_el += 1
avg = total_sum / total_el
print(a)
print(max_value)
print(min_value)
print(avg)