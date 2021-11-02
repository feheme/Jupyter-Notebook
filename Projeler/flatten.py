def flattenListe(liste):
    flatListe = liste
    düzListe = []


    for i in flatListe:
        if type(i) == int or type(i) == float or type(i) == str:
            düzListe.append(i)
        else:
            for a in i:
                if type(a) == int or type(a) == float or type(a) == str:
                    düzListe.append(a)
                else:
                    for b in a:
                        if type(b) == int or type(b) == float or type(b) == str:
                            düzListe.append(b)
                            




    print(düzListe)





input = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

flattenListe(input)