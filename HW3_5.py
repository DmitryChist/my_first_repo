n = list(map(str, input("Введите список элементов и нажмите Ентер (чем больше, тем лучше): ").split()))

len(n)
w = 0
for i in n:
    if n.count(i) >= 1:
        w +=1

print("Количество различных элементов", w)