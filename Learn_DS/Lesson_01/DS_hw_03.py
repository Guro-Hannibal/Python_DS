from itertools import combinations

a = 'loneliness'

b = 2


def foo(arg1, arg2):
    result = [el for el in combinations(arg1, arg2)]
    return result


print(foo(a, b))
