def tri_selection(tab):
    for i in range(len(tab)-1):
        indice_min = i
        for j in range(i+1, len(tab)):
            if tab[j] < tab[indice_min]:
                indice_min = j
        tab[i], tab[indice_min] = tab[indice_min], tab[i]
    return tab


#ou version plus découpée, se rapprochant plus de la description de l'algo :

def minimum(tab, i):
    """Recherche la position du minimum entre la position i et la fin du tableau tab"""
    ind_minimum = i
    for j in range(i+1, len(tab)):
        if tab[j] < tab[ind_minimum]:
            ind_minimum = j
    return ind_minimum

def echange(tab, i, j):
    tab[i], tab[j] = tab[j], tab[i]

def tri_selection(tab):
    for i in range(len(tab)-1):
        ind_minimum = minimum(tab, i)
        echange(tab, i, ind_minimum)
    return tab

print(tri_selection([1,52,6,-9,12]))