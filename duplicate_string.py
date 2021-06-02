a="good"
b="odg"
d=""
c=a+b
i=0
while i<len(c):
    if c[i] not in d:
        d+=c[i]
    i+=1
print(d)

# second_soul
a="good"
b="ood"
i=0
while i<len(a):
    if a[i] in b:
        print(a[i])
    i+=1
