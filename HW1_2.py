n = list(map(int, input("Введите список целых чисел через пробел и нажмите Ентер (чем больше, тем лучше): ").split()))
w = []
for i in n:
    if n.count(i) == 1:
        w.append(i)
print("Числа, которые не повторяется", w)