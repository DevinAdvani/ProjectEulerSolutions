
ways = 0
for i in range(0,2):
    recurrence1 = int((200-200*i)/100)+1
    for j in range(0,recurrence1):
        recurrence2 = int((200-200*i-100*j)/50)+1
        for k in range(0,recurrence2):
            recurrence3 = int((200-200*i-100*j-50*k)/20)+1
            for l in range(0,recurrence3):
                recurrence4 = int((200-200*i-100*j-50*k-20*l)/10)+1
                for m in range(0,recurrence4):
                    recurrence5 = int((200-200*i-100*j-50*k-20*l-10*m)/5)+1
                    for n in range(0,recurrence5):
                        recurrence6 = int((200-200*i-100*j-50*k-20*l-10*m-5*n)/2)+1
                        for o in range(0,recurrence6):
                            ways += 1
                            print(ways,i,j,k,l,m,n,o)
                            

