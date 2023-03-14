def read_input():
    in_str = input().split()
    x = in_str[0]
    x1 = in_str[2]
    sign = in_str[1]
    return int(x), int(x1), sign

def calculator(x, x1, sign):
    if sign == "+":
        return x + x1
    elif sign == "-":
        return x - x1
    elif sign == "*":
        return x * x1
    elif sign == "/":
        if x1==0:
            print("Знаменатель не может быть равен нолю!")
        else:
            return x / x1
