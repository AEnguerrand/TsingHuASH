def score(Tag1,Tag2):
    # Tag1 et Tag2 listes de tags ex: ["cat", "banana", "b"]
    # Calcule l'intersection puis retire la taille de l'intersection aux 2 autres sections pour avoir la taille de la partie exclue A\B
    Set1,Set2 = set(Tag1),set(Tag2)
    inc = len(Set1.intersection(Set2))
    ex1 = len(Set1) - inc
    ex2 = len(Set2) - inc
    return min([inc,ex1,ex2])

def tags_applatis(Chemin, Pictures):
    # Prends la liste des id des images dans le chemin, en doublon si 2 verticaux [1, (2,5),4]
    # et le fichier des images
    # Renvoie la liste des tags des images (en fusionnant si 2 verticaux)
    applati = []
    for x in Chemin:
        if type(x) == int:
            applati.append(Pictures[x][2:])
        else:
            V1 = set(Pictures[x[0]][2:])
            V2 = set(Pictures[x[1]][2:])
            applati.append(list(V1.union(V2)))
    return applati


def score_final(Chemin, Pictures):
    #Calcule le score final en créant d'abord une liste des tags applatis
    ScoreFinal =  0
    T = tags_applatis(Chemin,Pictures)
    for i in range(len(Chemin)-1):
        ScoreFinal += score(T[i],T[i+1])
    return ScoreFinal
