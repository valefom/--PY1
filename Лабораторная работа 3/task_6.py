list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO Оформить решение
max_val = max(list_numbers)
max_idx = -1
for i, j in enumerate(list_numbers):
    if j == max_val:
        max_idx = i

list_numbers[max_idx] = list_numbers[-1]
list_numbers[-1] = max_val
print(list_numbers)
