def swap_special(L,i,j):
    # Swap les éléments aux positions i et j tout en minimisant la variation de score en gardant un maximum de paires communes
    swapped_L = L[:i] + [L[j]] + list(reversed(L[i+1:j])) + [L[i]] + L[j+1:]
    return swapped_L

def swap_triolisme(L,i,j,k):
    swapped_L = L[:i] + [L[k]] + list(reversed(L[j+1:k])) + [L[i]] + L[i+1:j] + [L[j]] + L[k+1:]
    return swapped_L

def trieur_orientation(Pictures):
    # Renvoie la liste des id avec d'abord les indices horizontaux puis les indices verticaux par paires arbitraires
    # Ex: [5,4,8,9,(1,2),(6,7)] 
    H = []
    V = []
    paire = -1
    for i in range(len(Pictures)):
        x = Pictures[i]
        if x[1] == 'H':
            H.append(i)
        else:
            if paire == -1:
                paire = i
            else:
                V.append((paire,i))
                paire = -1
    if paire !=-1:
        print('vertical tout seul!!!')
    return H + V
