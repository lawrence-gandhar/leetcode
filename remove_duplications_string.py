txt = "babcddcbertedfs hgkhl gjgoyho  hlhlhpjp;j iuohpojpojpjijlj jhfjgkhk"
temp = []
x = iter(txt)
while True:
    try:
        hh = next(x)
        print(hh)
        print(txt.count(hh), hh)
        if txt.count(hh) > 1:
            if txt.find(hh) != -1:
                f = list(txt.partition(hh))
                print(f)
                temp.append(f[1])
                f[2] = f[2].replace(hh, "")
                txt = f[2]
                x = iter(txt)
        else:
            temp.append(hh)
    except:
        print(''.join(temp))
        break