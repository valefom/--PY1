import random

def get_unique_list_numbers() -> list[int]:
    l = []
    while True:  # TODO написать функцию для получения списка уникальных целых чисел
        d = [x for x in range(-10,10)]
        while True:
            a = random.choice(d)
            if a not in l:
                l.append(a)
            if len(set(l)) == 15:
                return l

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
