

def raise_to_power(base, pow):
    res = 1
    for i in range(pow):
        res = res * base

    return res


print(raise_to_power(2, 2))


