import io, random, sys

def kysely(sanat):
    kielet = sanat[0]
    kieli = 'ei tietoa'
    while kieli not in kielet:
        kieli = input('Valitse kysyttävä (' + kielet[0] + ', ' + kielet[1] + '): ')
    vastaus = kielet.index(kieli)
    kysymys = 1 - vastaus
    print(kielet[kysymys], '->', kielet[vastaus], '\tLopetus: lopeta')
    while True:
        n = random.randrange(1, len(sanat))
        sanapari = sanat[n]
        for i in range(3):
            sana = input(sanapari[kysymys] + ': ')
            if sana == sanapari[vastaus]:
                print('Oikein!')
                break
            elif sana == 'lopeta':
                return
            elif i == 2:
                print('Väärin.', sanapari[vastaus])
            else:
                print('Väärin. Yritä uudelleen.')
    
def lue(tiedosto):
    sanat = []
    with io.open(tiedosto, mode="r", encoding="utf-8") as f:
        for rivi in f:
            pari = rivi.strip('\n').split('\t')
            if len(pari) == 2:
                sanat.append(pari)
            else:
                print('Virhe:', pari)
    return sanat

if len(sys.argv) == 2:
    tiedosto = sys.argv[1]
else:
    tiedosto = input('Anna tiedostonimi: ')
sanat = lue(tiedosto)
kysely(sanat)
