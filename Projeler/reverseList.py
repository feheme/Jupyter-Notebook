def reverseList(liste):
    yeniListe = []
    for a in liste:
        yeniListe.append(a[::-1])
    yeniListe = yeniListe[::-1]  
    print(yeniListe)

input =  [[1, 2], [3, 4], [5, 6, 7]]
reverseList(input)