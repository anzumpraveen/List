a=[4,5,6,7,8,9,10]
n=int(input("enter the num"))
i=0
while i<len(a):
    if n==a[i]:
        e=("yes")
        break
    else:
        e=("no")
    i+=1
print(e)
