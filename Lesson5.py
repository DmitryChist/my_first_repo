import random

x = (random.randint(1,6))
y = (random.randint(1,6))
print(x)
print(y)
answer = input("Бросить кубики ещё? ")
while answer == "Да":
    x = (random.randint(1, 6))
    y = (random.randint(1, 6))
    print(x)
    print(y)
    answer = input("Бросить кубики ещё? ")


