def produs_generic(*args):
    if len(args) == 2:
        return produs(*args)

    p = 1
    for arg in args:
        p = p * arg
    return p


def produs(a, b):
    return a * b


def sum(*args):
    s = 0
    for arg in args:
        s += arg # s = s + arg
    return s

def trim(s):
    return s.strip()


def upper_case(s):
    return s.upper()


def convert_input(s, f):
    return f(s)


def function_selection(s):
    if s == "trim":
        return trim
    else:
        return upper_case

map_f = {
    "trim": trim,
    "upper": upper_case
}


if __name__ == "__main__":
    a = produs(10, 20)
    b = produs_generic(20, 20, 30, 30)

    p = produs

    # operations = [sum, produs, produs_generic]
    # s1 = operations[0](10, 20)
    # s2 = operations[2](10, 20, 20, 10)
    #
    # print(s1, s2)

    # procesari = [trim, upper_case]
    # i = input()
    # print(i)
    # for f in procesari:
    #     i = f(i)
    # print(i)
    #
    # proces = input()
    #
    # r = map_f[proces](i)
    # print(r)

    s = convert_input("name   ", trim)
    print(s)

    f = function_selection("trim")
    s = f("   dsads  ")
    print(s)

    f = lambda x, y: x + y
    # def f(x, y):
    #     return x + y
    print(f(2, 2))

    s3 = convert_input("NAME", lambda x: x.lower())
    print(s3)

    colectie = ["asn", "dnfe", "dasfgy"]
    r = map(upper_case, colectie)
    print(r)
    for ri in r:
        print(ri)

    # r = []
    # for entry in colectie:
    #     r.append(upper_case(entry))

    r2 = map(lambda x: x.title(), map(upper_case, colectie))
    print(list(r2))

    f1 = filter(lambda x: x[0] == 'a', colectie)
    print(f1)
    print(list(f1))