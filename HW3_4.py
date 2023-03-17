n = list(map(int, input("Введите список целых чисел через пробел и нажмите Ентер (чем больше, тем лучше): ").split()))

def change():
    x = 0
    for i in range(1, len(n)-1):
        if n[i] > n[i-1] and n[i] > n[i+1]:
            x = x + 1
        return x

print(x)