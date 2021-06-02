n=int(input("enter the num"))
org=n
c=0
s=0
i=1
while i<n:
    if org>=i:
        s+=i
        c+=1
        org-=i
    i+=1
print(c)

