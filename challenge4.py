def cha1(x):
    return x ** 2


def cha2(x):
    print(x)


def cha3(a,b,x=4,y=7,z=5):
    return x + y + z + a + b


def cha4(x):
    return x / 2

def cha42(x):
    return x * 4

a = cha4(20)
b = cha42(a)
print(b)


def cha5(x):
    try:
        return float(x)
    except ValueError:
        print("数字を入れろ")

print(cha5("11"))
