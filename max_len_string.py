a='muska'
b='anzum'
c=[]
i=0
x=0
while i<len(a):
    if a[i]not in b:
        c.append(a[i])
        x+=1
    i+=1
    j=0
    d=[]
    y=0
    while j<len(b):
        if b[j]not in a:
            d.append(b[j])
            y+=1
        j+=1
if x>y:
    print("big length of",a)
else:
    print("small length of",b)
print(d,y)
print(c,x)

