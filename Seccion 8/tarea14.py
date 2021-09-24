def toFar(temp):
    temp = (temp * 9/5) + 32
    return temp


def toCel(temp):
    temp = (temp - 32) * 5/9
    return temp


print(toFar(35))
print(toCel(95))
