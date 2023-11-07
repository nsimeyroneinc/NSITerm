def fabrique(h, n):
    def annexe(hauteur_max):
        nonlocal n
        if n == 0 :
            return []
        elif hauteur_max == 0:
            n=n-1
            return [[],[]]
        else:
            n=n-1
            gauche = annexe(hauteur_max - 1)
            droite = annexe(hauteur_max - 1)
            return [[gauche],[droite]]
    return annexe(h)

print(fabrique(5,7))