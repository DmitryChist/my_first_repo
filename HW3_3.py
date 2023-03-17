lst = list(map(str, input("Введите список элементов и нажмите Ентер (чем больше, тем лучше): ").split()))
def change(lst):
    n = len(lst)
    x = lst[0]
    lst[0] = lst[n-1]
    lst[n-1] = x
    return lst

print(change(lst))






