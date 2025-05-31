salary = float(input("Введите сумму вашей ЗП "))
credit = float(input("Укажите сумму ежемесячных платежей по кредиту "))
utility_bills = float(input("Укажите сумму ежемесячных коммунальнах платежей "))
balans = salary - credit - utility_bills
print ("Итого после всех выплат составляет ", balans)
