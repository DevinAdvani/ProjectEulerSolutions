
def E(n):
    return (1504170715041707*n)%4503599627370517

list = [E(1)]


for i in range(2,9999999):
    if E(i) < list[-1]:
        list.append(i)

print(list)
