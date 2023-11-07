def recherche(x,l):
    for elt in l:
        if elt==x:
            return True
    return False


L=[1,3,5,7,11,13]

def recherche_dichotomique(tab, val) :
    '''
    renvoie True ou False suivant la présence de la valeur val dans le tableau trié tab.
    '''
    i_debut = 0
    i_fin = len(tab) - 1
    while i_debut <= i_fin :
        i_centre = (i_debut + i_fin) // 2     # 
        val_centrale = tab[i_centre]          #  
        if val_centrale == val:               #  
            return True
        if val_centrale < val:                #  
            i_debut = i_centre+1              #  
        else :
            i_fin = i_centre-1
    return False

tab = [1, 5, 7, 9, 12, 13]
recherche_dichotomique(tab, 12)==True
recherche_dichotomique(tab, 17)==False


def dicho_rec_2(tab, val, i=0, j=None): # 
    if j is None:                       # 
        j = len(tab)-1
    if i > j :
        return False
    m = (i + j) // 2
    if tab[m] < val :
        return dicho_rec_2(tab, val, m + 1, j)
    elif tab[m] > val :
        return dicho_rec_2(tab, val, i, m - 1 )
    else :
        return True

print(dicho_rec_2(tab, 17))