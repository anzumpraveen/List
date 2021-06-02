n=input("enter the string value")
x=[" !","#","$","%","&","(",")","*","+","-","/",":",";",'<','=','>',"?","@","_","~"]
i=0
while i<len(n):
    if n[i] not in x:
        print(n[i],end="")
        i+=1
    else:
        i+=1


