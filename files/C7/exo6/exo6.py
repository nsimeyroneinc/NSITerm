def echange(liste,i,j):
    liste[i],liste[j] = liste[j],liste[i]

def min_liste(liste,ind):
    elt_min = liste[ind]
    ind_min=ind
    for k in range(ind,len(liste)):
        if liste[k]<elt_min:
            elt_min=liste[k]
            ind_min=k
    return ind_min

def tri_selection(liste):
    liste_nouv=[]
    for elt in liste:
        liste_nouv.append(elt)
    longueur = len(liste_nouv)
    for ind in range(longueur):
        ind_min = min_liste(liste_nouv,ind)
        echange(liste_nouv,ind,ind_min)
    return liste_nouv

L=[12,19,10,13,11,15,9,14]

L1=tri_selection(L)
print(L)
print(L1)

def tri_insertion(liste):
    liste_nouv=[]
    for elt in liste:
        liste_nouv.append(elt)
    for ind in range(0,len(liste_nouv)-1):
        j = ind
        while liste_nouv[j+1]<liste_nouv[j] and j>=0:
            echange(liste_nouv,j,j+1)
            j=j-1
    return liste_nouv

L2=tri_insertion(L)
print(L)
print(L2)