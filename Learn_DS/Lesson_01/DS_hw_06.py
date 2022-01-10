from itertools import chain

demo = [[4, 2, 6, 3, 7, 2, 7, 4, 4, 9, 7, 24], [8, 2, 6, 14, 2, 4, 7, 4, 24, 9, 7, 24]]


def foo(demo):
        result = 0
        for i in demo:
            max = 0
            for yot in i:
                if yot > max:
                    max = yot
            result += (pow(max, 2))
            print(result)
        result %= 2
        return result


print(foo(demo))


# $(a_1^2 + a_2^2 + ... + a_n^2) % m $