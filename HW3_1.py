def calc1():
    prim = input().split()
    print(prim)
    x = prim[0]
    y = prim[2]
    sign = prim[1]
    return int(x), int(y), sign

def calc(x, y, sign):
    if sign == "+":
        return x + y
    elif sign == "-":
        return x - y
    elif sign == "*":
        return x * y
    elif sign == "/":
        if y == 0:
            print("На ноль делить нельзя")
        else:
            return x / y

x, y, sign = calc1()
print(calc(x, y, sign))

