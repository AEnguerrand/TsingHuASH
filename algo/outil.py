def swap_special(L,i,j):
    #Swap les éléments aux positions i et j tout en minimisant la variation de score en gardant un maximum de paires communes
    swapped_L = L[:i] + [L[j]] + list(reversed(L[i+1:j])) + [L[i]] + L[j+1:]
    return swapped_L
print(swap_special([1,2,3,4,5,6,7,8,9],1,7))