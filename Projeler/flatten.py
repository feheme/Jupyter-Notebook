def flattenListe(liste):
    flatListe = liste
    düzListe = []


    for i in flatListe:
        if type (i) == list:
            for a in i:
                if type(a) == list:
                    for b in a:

                        if type(b) == list:
                            for c in b:
                                düzListe.append(c)

                        else:

                            düzListe.append(b)
                        
                else:
                    düzListe.append(a)
        else:
            düzListe.append(i)


    print(düzListe)





input = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

flattenListe(input)