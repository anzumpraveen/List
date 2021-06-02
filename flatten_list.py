a=[1,2,3,[4,[5,6,[7]],8],[9]]
b=[]
def fun(a):
    for i in a:
        if type(i)==list:
            fun(i)
        else:
            b.append(i)
print(a)
fun(a)
print(b)