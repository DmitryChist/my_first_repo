cars = list(map(str, input("Введите название машин ").split()))
names = list(map(str, input("Введите имена ").split()))
cars.sort()
names.sort()
result_list = list(zip(names, cars))
print(result_list)
