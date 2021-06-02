list=[[3,5,2,4],[2,7,1,3],[6,3,5,5],[1,2,3,4]]
i=0
while i<len(list):
    j=0
    multi=1
    while j<len(list):
        multi=list[j][i]+multi
        j=j+1
    i=i+1
    print(multi)