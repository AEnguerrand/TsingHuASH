
def score(Tag1,Tag2):
    # Tag1 et Tag2 listes de tags ex: ["cat", "banana", "b"]
    # Calcule l'intersection puis retire la taille de l'intersection aux 2 autres sections pour avoir la taille de la partie exclue A\B
    Set1,Set2 = set(Tag1),set(Tag2)
    inc = len(Set1.intersection(Set2))
    ex1 = len(Set1) - inc
    ex2 = len(Set2) - inc
    return min([inc,ex1,ex2])

def pic_to_tags(x,Pictures):
    #renvoie une liste de tags à partir d'un indice ou un couple d'indices
    if type(x) == int:
        return Pictures[x][2:]
    V1 = set(Pictures[x[0]][2:])
    V2 = set(Pictures[x[1]][2:])
    return list(V1.union(V2))
    
def tags_applatis(Chemin, Pictures):
    # Prends la liste des id des images dans le chemin, en doublon si 2 verticaux [1, (2,5),4]
    # et le fichier des images
    # Renvoie la liste des tags des images (en fusionnant si 2 verticaux)
    applati = []
    for x in Chemin:
        tags = pic_to_tags(x,Pictures)
        applati.append(tags)
    return applati

def score_final(Chemin, Pictures):
    #Calcule le score final en créant d'abord une liste des tags applatis
    ScoreFinal =  0
    T = tags_applatis(Chemin,Pictures)
    for i in range(len(Chemin)-1):
        ScoreLocal = score(T[i],T[i+1])
        ScoreFinal += ScoreLocal
        print('De ' + str(Chemin[i]) + ' à ' +  str(Chemin[i+1])+ ' : ' + str(ScoreLocal))
    return ScoreFinal

def eval_swap(L,i,j,Pictures):
    #Evalue le gain en effectuant le swap i,j sur le chemin L
    a,b = L[i],L[j]
    a,b = pic_to_tags(a,Pictures), pic_to_tags(b,Pictures)
    c,d = [] if i ==0 else pic_to_tags(L[i-1],Pictures), [] if j == len(L)-1 else pic_to_tags(L[j+1],Pictures)
    return score(c,b) + score(a,d) - score(c,a) - score(b,d)