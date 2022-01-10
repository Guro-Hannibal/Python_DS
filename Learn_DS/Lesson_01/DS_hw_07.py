def foo(n):
    result = [0]
    for i in range(n):
        if i > 1:
            result.append(result[i] + result[i-1])
        else:
            result.append(1)
    return result


print(foo(10))

