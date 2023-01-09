nums = {1,2,3,4,5,6,7,8,9}
list = []
a = 10

for totals in range(6,28):
    for b in nums:
        c = totals-a-b 
        for d in nums-{b,c}:
            e = totals-d-c 
            for f in nums-{b,c,d,e}:
                g=totals-f-e 
                for h in nums-{a,b,c,d,e,f,g}:
                    i = totals-g-h 
                    j = totals-b-i
                    print(a,b,c,d,e,f,g,h,i,j)
                    if {b,c,d,e,f,g,h,i,j} == nums:
                        start = min(d,f,h,j)
                        if start == d:
                            list.append([d,c,e,f,e,g,h,g,i,j,i,b,a,b,c])
                        if start == f:
                            list.append([f,e,g,h,g,i,j,i,b,a,b,c,d,c,e])
                        if start == h:
                            list.append([h,g,i,j,i,a,b,c,d,c,e,f,e,g])
                        if start == j:
                            list.append([j,i,b,a,b,c,d,c,e,f,e,g,h,g,i])

newlist = []         
for i in range(0,len(list)):
    output = ""
    for j in range(0,len(list[i])):
        output += str(list[i][j])
    newlist.append(output)
    
print(max(newlist))