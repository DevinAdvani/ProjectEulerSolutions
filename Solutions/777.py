import matplotlib.pyplot as plt
import math

x = []
y = []
c = []
t = []
xic = []
yic = []
n = 5
a = 4
b = 7

xstart = -1
step = 0.01
while xstart < 1:
    c.append((1/a)*math.acos(xstart))
    xstart += step

t = sorted(c)

for i in range(0,len(t)):
    x.append(math.cos(a*t[i]))
    y.append(math.cos(b*(t[i]-(math.pi/10))))




def plot(): # plots the function
        plt.scatter(x,y)
        plt.show()

def m(x1,y1,x2,y2): # finds the gradient of mx+c
    g = (y2-y1)/(x2-x1)
    return g

def c(x1,y1,x2,y2): # fins the constant of mx+c
    m = (y2-y1)/(x2-x1)
    h = y1 - (m*x1)
    return h

def xintersect(x1,y1,x2,y2,x3,y3,x4,y4): #returns the x coordinate of intersection if there is one
    m1 = m(x1,y1,x2,y2)
    c1 = c(x1,y1,x2,y2)
    m2 = m(x3,y3,x4,y4)
    c2 = c(x3,y3,x4,y4)
    if m1 != m2 and min(x1,x2)<((c2-c1)/(m1-m2))<max(x1,x2) and min(x3,x4)<((c2-c1)/(m1-m2))<max(x3,x4) and min(y1,y2)<(m1*((c2-c1)/(m1-m2)) + c1)<max(y1,y2) and min(y3,y4)<(m1*((c2-c1)/(m1-m2)) + c1)<max(y3,y4) and round(m1,2) != round(m2,2):
        return ((c2-c1)/(m1-m2))

def d():
    for e in range(0,int(360*n)):
        for f in range(0,int(360*n)):
            if xintersect(x[e],y[e],x[e+1],y[e+1],x[f],y[f],x[f+1],y[f+1]) != None:
                xic.append(round(xintersect(x[e],y[e],x[e+1],y[e+1],x[f],y[f],x[f+1],y[f+1]),2))
                #yic.append(round(m(x[e],y[e],x[e+1],y[e+1])*xintersect(x[e],y[e],x[e+1],y[e+1],x[f],y[f],x[f+1],y[f+1])+c(x[e],y[e],x[e+1],y[e+1])),2)
                print(set(xic))
