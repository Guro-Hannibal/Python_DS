l1 = [1, 2, 3]

l2 = [15, 25]


def foo(a, b):
    result = []
    for i in a:
        for z in b:
            result.append({f'{i},{z}': i * z})
    return result


print(foo(l1, l2))
