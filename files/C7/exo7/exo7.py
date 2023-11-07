def est_trie(liste):
    long=len(liste)
    for ind in range(long-1):
        if liste[ind+1]<liste[ind]:
            return False
    L_nv=L.reverse()
    est_trie(L_nv)
    return True

L=[12,9,17,11,3]
L_nv=L.reverse()
print(L_nv)
L2=[1,2,3,4,5,6,7,8]

#print(est_trie(L))

#print(est_trie(L2))