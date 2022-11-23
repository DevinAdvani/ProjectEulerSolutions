count = 0

for one in range(0,201):
    for two in range(0,101):
        for five in range(0,41):
            for ten in range(0,21):
                for twenty in range(0,11):
                    for pound in range(0,3):
                            if 100 == one*1 + two*2 + five*5 + ten*10 + twenty*20 + pound*100:
                                count += 1
                                print(one,two,count)
#add one as removed 2 pound
