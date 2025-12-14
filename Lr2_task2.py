money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
month = 0
while True:
    if month == 0:
        money_capital = money_capital + salary - spend
        month += 1
    else:
        spend = spend * (1 + increase)
    money_capital = money_capital + salary - spend
    month += 1
    if money_capital < spend:
        break



print("Количество месяцев, которое можно протянуть без долгов:", month)
