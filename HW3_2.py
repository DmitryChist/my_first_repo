n = int(input("Введите количество лет "))
m = int(input("Введите сумму вклада "))

def bank(n, m):
    prim = m + ((m * 5 * n)/100)
    return prim

print("Сумма вклада", bank(n, m))
