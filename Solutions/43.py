nums = {0,1,2,3,4,5,6,7,8,9}
d6set = {0,5}
count = 0
for d4 in range(0,9,2):
    for d6 in (d6set)-{d4}:
        for d3 in nums-{d4,d6}:
            for d5 in nums-{d4,d3,d6}:
                if (d3+d4+d5)%3 == 0:
                    for d7 in nums-{d3,d4,d5,d6}:
                        if int(str(d5)+str(d6)+str(d7))%7 == 0:
                            for d8 in nums-{d3,d4,d5,d6,d7}:
                                if int(str(d6)+str(d7)+str(d8))%11 == 0:
                                    for d9 in nums-{d3,d4,d5,d6,d7,d8}:
                                        if int(str(d7)+str(d8)+str(d9))%13 == 0:
                                            for d10 in nums-{d3,d4,d5,d6,d7,d8,d9}:
                                                if int(str(d8)+str(d9)+str(d10))%17 == 0:
                                                    for d2 in nums-{d3,d4,d5,d6,d7,d8,d9,d10}:
                                                        for d1 in nums-{d2,d3,d4,d5,d6,d7,d8,d9,d10}:
                                                            count += (int(str(d1)+str(d2)+str(d3)+str(d4)+str(d5)+str(d6)+str(d7)+str(d8)+str(d9)+str(d10)))
                                                            
print(count)