user=input("ente the word/sentence: ")
name=user.split(" ")
i=0
a=[]
b=[]
while i<len(name):
    j=0
    sum=0
    while j<len(name[i]):
        sum+=ord(name[i][j])
        j+=1
    a.append(sum)
    b.append(name[i])
    k=0
    while k<len(a):
        if a[i]<a[k]:
            b[i],b[k]=b[k],b[i]
        k=k+1    
    i+=1
print(a)
print(b)




