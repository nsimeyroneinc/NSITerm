def echange(tab, i, j):
    tab[i], tab[j] = tab[j], tab[i]

def tri_iteratif(tab):
    for k in range(len(tab)-1, 0, -1):
        indice_max = k
        for i in range(0, k):
            if tab[i] > tab[indice_max]:
                indice_max = i
        echange(tab, k, indice_max)
    return tab

print(tri_iteratif([41, 55, 21, 18, 12, 6, 25]))