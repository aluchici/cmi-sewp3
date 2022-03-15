def f(g):
    print("Am decorat functia", g)
    return g


@f
def suma(*args):
    s = 0
    for arg in args:
        s += arg
    return s


@f
def produs(*args):
    p = 1
    for arg in args:
        p *= arg
    return p


def nested_function(a, b):
    print("Outside")

    def inner_function(a, b):
        print("Inside", a, b)

    inner_function(a, b)
    return inner_function


s = suma(10, 20, 30)
print(s)
p = produs(10, 20)
print(p)

nested_function(10, 20)