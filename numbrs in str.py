# numbers-in-string
i=str(input())
if len(i)<=1000:
    count=0
    for x in range(len(i)):
        
        if(i[x].isnumeric()):
            count+=1
    print(count)
