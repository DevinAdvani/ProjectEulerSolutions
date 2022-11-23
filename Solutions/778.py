'''
If  are two nonnegative integers with decimal representations  and  respectively, then the freshman's product of  and , denoted , is the integer  with decimal representation  such that  is the last digit of .
For example, .

Let  be the sum of  for all sequences of integers  with .
For example, , and .

Find , give your answer modulo
'''
def fp(a,b):#freshman's product
    d = []
    for i in range(0,len(str(a))):
        d.append(str(int(str(a)[i])*int(str(b)[i]))[-1])
    e = "".join(d)
    return int(e)

def F(R,M):
