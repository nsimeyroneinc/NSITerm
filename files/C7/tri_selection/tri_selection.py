from random import randint

def tri_selection(lst) :
    for k in range(len(lst)-1):
        indice_min = k
        for i in range(k+1, len(lst)) :
            if lst[i] < lst[indice_min]:
                indice_min = i
        print(lst)
        lst[k], lst[indice_min] = lst[indice_min], lst[k]
        print(lst)

#ex_liste = [randint(1,100) for _ in range(50)]

#{L=["P","R","O","G","R","A","M","M","E"]
#print(L)

L=[8,12,6,19]
tri_selection(L)
#print(L)