def f(n,d):
    result = ""
    repeatslist = []
    addon = ""
    while True:
        if d > n:
            n *= 10
            if n == 10:
                pass 
            else:
                addon += "0"
            if len(result) == 0:
                result += "0."
        else:
            r = n % d
            addon += str(int((n-r)/d))
            result += addon
            if [r,n,addon] in repeatslist:
                index = repeatslist.index([r,n,addon])
                print(repeatslist)
                return len(repeatslist)-index
            repeatslist.append([r,n,addon])
            print(repeatslist)
            print(result)
            addon = ""
            #if r == 0:
            #    return 0
            n = r
        if len(result) == 20:
            return result
                
print(f(1,13))