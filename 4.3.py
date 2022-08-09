p = int(input())  # pocket
g = 'зеленый'  # green
r = 'красный'  # red
b = 'черный'  # black
e = 'ошибка ввода'  # error_message
if p == 0:
    print(g)
elif p % 2 == 0 and p >= 1 <= 10:
    print(b)
elif p % 2 == 0 and 19 <= p <= 28:
    print(b)
elif p % 2 == 0 and 11 <= p <= 18:
    print(r)
elif p % 2 == 0 and 29 <= p <= 36:
    print(r)
else:
    print(e)