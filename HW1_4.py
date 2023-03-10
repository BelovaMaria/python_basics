print("Сумма выручки: ")
rev = input()
print("Сумма издержек: ")
exp = input()
print("Количество сотрудников в компании: ")
staff = input()
n = ((int(rev) - int(exp)) / int(staff))
if rev > exp:
    print("Прибыль в расчете на 1 сотрудника: ", n)
elif rev < exp:
    print("Сумма издержек превышает доход")
elif rev == exp:
    print("Сумма издержек равна доходу")
