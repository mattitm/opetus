etu = (24, 34, 42)
taka = (32, 28, 24, 21, 18, 16, 14, 12)
vaihteet = []

for e in range(len(etu)):
    for t in range(len(taka)):
        valitys = float(etu[e])/float(taka[t])
        i = len(vaihteet)
        for v in range(i):
            if valitys < vaihteet[v][2]:
                i = v
                break
        vaihteet.insert(i, (e+1, t+1, valitys))

for v in range(len(vaihteet)):
    print(v+1, vaihteet[v])
