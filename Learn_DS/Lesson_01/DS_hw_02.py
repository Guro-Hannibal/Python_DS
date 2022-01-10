from itertools import permutations

demo = 'Loneliness'

num = 2


def foo(a, b):
    result = [el for el in permutations(a, b)]
    return result


print(foo(demo, num))
