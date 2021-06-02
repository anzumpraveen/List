a="my name is anzum"
b=a.split()
str=" "
i=0
while i<len(b):
    j=0
    while j<len(b[i]):
        if j==0:
            str+=b[i][j].upper()
        else:
            str+=b[i][j]
        j+=1
    str+=" "
    i+=1
print(str)
