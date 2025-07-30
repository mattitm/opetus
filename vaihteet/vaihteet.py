etu = (24, 34, 42)
taka = (32, 28, 24, 21, 18, 16, 14, 12)
vaihteet = []

for e in range(len(etu)):
    for t in range(len(taka)):
        valitys = float(etu[e])/float(taka[t])
        i = len(vaihteet)
        while i > 0 and valitys < vaihteet[i-1][2]:
            i -= 1
        vaihteet.insert(i, (e+1, t+1, valitys))

for v in range(len(vaihteet)):
    print(v+1, vaihteet[v])
