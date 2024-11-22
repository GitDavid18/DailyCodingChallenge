def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


def get_first(a, b):
    return a


def get_last(a, b):
    return b


def car(i):
    return i(get_first)
    # return i(lambda a, b: a)


def cdr(i):
    return i(get_last)
    # return i(lambda a, b: b)


x = cons(3, 4)
print(cons)
print(car(x))
print(cdr(x))
