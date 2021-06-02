a=[50,40,210,23,70,57,12,5,10,7]
max=0
max1=0
i=0
while i<len(a):
    if a[i]>max :
        max=a[i]
    if max>a[i]>max1:
        max1=a[i]
    i+=1
print(max1)
print(max)