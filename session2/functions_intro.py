def adunare(a, b):
    c = a + b
    return c


a = adunare(1, 1)
b = adunare(2, 3)
c = adunare(5, 5)

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

if adunare(1, 1) > 1:
    print("Da")
else:
    print("Nu")

def find_key(d, v):
    for key, value in d.items():
        if value == v:
            return key


def random_function_name(a, b, c=0, *args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    if len(args):
        print(args[0])
    else:
        print("Missing args")

    if "t" in kwargs.keys():
        print(kwargs["t"])
    else:
        print("Missing t arg")

    if 100 in kwargs.values():
        k = find_key(kwargs, 100)
        print(k)


random_function_name(b=1, a=2, c=20)
random_function_name(b=1, a=2, r=100)


def adunare2(*args):
    s = 0
    for si in args:
        s = s + si
    return s


s1 = adunare2(1, 2, 3, 4, 5, 6)
s2 = adunare2(2, 3, 4)

print(f"s1 = {s1}")
print(f"s2 = {s2}")
