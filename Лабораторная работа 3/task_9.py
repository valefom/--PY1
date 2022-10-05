salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

# TODO Оформить решение
total = 0
for i in range(11):
    if i > 0:
        need_money += abs(salary - spend)
        spend *= 1+increase

print(round(need_money))
