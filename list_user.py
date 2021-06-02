a=[82,35,41,8,9,75]
n=int(input("enter = :"))
i=0
while i<(len(a)-n):
    j=i
    while j<(i+n):
        print(a[j],end=" ")
        j+=1
    print()
    i+=1
while i< len(a):
    print(a[i],end=" ")
    i+=2