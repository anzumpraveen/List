def catAndMouse(x, y, z):
    if x ==0:
        return "Cat B"
    if y == 0:
        return "Cat A"
    a = x-z
    b = y-z
    if a<0:
        a=a*-1
    if b<0:
        b=b*-1
    if a == b:
        return "Mouse C"
    elif a > b:
        return "Cat B"
    else:
        return "Cat A"
print(catAndMouse(1,2,3))