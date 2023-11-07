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
    longueur = len(liste)
    for ind in range(longueur):
        ind_min = min_liste(liste,ind)
        echange(liste,ind,ind_min)

L=[12,19,10,13,11,15,9,14]



def echange(liste,i,j):
    liste[i],liste[j] = liste[j],liste[i]

def max_liste(liste,ind):
    elt_max = liste[ind]
    ind_max=ind
    for k in range(ind,len(liste)):
        if liste[k]>elt_max:
            elt_max=liste[k]
            ind_max=k
    return ind_max

def tri_selection_inverse(liste):
    longueur = len(liste)
    for ind in range(longueur):
        ind_max = max_liste(liste,ind)
        echange(liste,ind,ind_max)

L=[12,19,10,13,11,15,9,14]


def tri_insertion_inverse(liste):
    for ind in range(0,len(liste)-1):
        j = ind
        while liste[j+1]>liste[j] and j>=0:
            echange(liste,j+1,j)
            j=j-1

tri_insertion_inverse(L)
print(L)