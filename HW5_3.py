import itertools
n = list(map(int, input("Введите список числа через запятую и пробел, затем нажмите Ентер (чем больше, тем лучше): ").split(', ')))
m = list(itertools.permutations(n))
print(m)