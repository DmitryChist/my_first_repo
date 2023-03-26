n = list(map(int, input("Введите список числа через пробел, затем нажмите Ентер (чем больше, тем лучше): ").split()))
def sum_n(*args):
    sp=[i for i in n]
    return sum(sp)
print("Сумма =", sum_n())