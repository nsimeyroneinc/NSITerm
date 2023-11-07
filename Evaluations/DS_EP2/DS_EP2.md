---
title : Thème  - Epreuve pratique
subtitle: 
subsubtitle: Terminale NSI
author : M.Meyroneinc-Condy
numbersections: true
fontsize: 10pt
geometry:
- top=20mm
- left=20mm
- right=20mm
- heightrounded    
--- 


<table  class="yellowTable">
        <tr >
            <th width="20%"; style="background-color: #3B444B;color:white;text-align:center;border:none;font-size:40pt;">
            02
            </th>
            <th  class="yellowTh";width="80%"; style="text-align:center;border:none;font-size:25pt;">Epreuve Pratique</th>
        </tr>
</table>
<br>


## Exercice 1 

!!! exo 
    === "Enoncé"
        Sur le réseau social TipTop, on s’intéresse au nombre de « like » des abonnés. Les données sont stockées dans des dictionnaires où les clés sont les pseudos et les valeurs correspondantes sont les nombres de « like » comme ci-dessous :

        ```python
        {'Bob': 102, 'Ada': 201, 'Alice': 103, 'Tim': 50}
        ```

        Écrire une fonction `top_like` qui :

        - Prend en paramètre un dictionnaire likes non vide dont les clés sont des chaînes de caractères et les valeurs associées sont des entiers ;  
        -  Renvoie un tuple dont :  
            - La première valeur est la clé du dictionnaire associée à la valeur maximale ; en cas d'égalité sur plusieurs clés, on choisira la plus petite suivant l'ordre alphabétique  
            - La seconde valeur est la valeur maximale présente dans le dictionnaire.  

        Exemples :
        ```python
        >>> top_like({'Bob': 102, 'Ada': 201, 'Alice': 103, 'Tim': 50})
        ('Ada', 201)
        >>> top_like({'Alan': 222, 'Ada': 201, 'Eve': 222, 'Tim': 50})
        ('Alan', 222)
        ```

    === "Solution 1"
        ```python
        def top_like(likes):
            top_pseudo = None
            top_nb_likes = 0
            for pseudo in likes:
                nb_likes = likes[pseudo]
                if nb_likes > top_nb_likes or nb_likes == top_nb_likes and pseudo < top_pseudo:
                    top_pseudo = pseudo
                    top_nb_likes = nb_likes
            return top_pseudo, top_nb_likes
        ```
    === "Solution 2 : avec la méthode `items`"
        ```python
            def top_like(likes):
                top_pseudo = None
                top_nb_likes = 0
                for pseudo, nb_likes in likes.items():
                    if nb_likes > top_nb_likes or nb_likes == top_nb_likes and pseudo < top_pseudo:
                        top_pseudo = pseudo
                        top_nb_likes = nb_likes
                return top_pseudo, top_nb_likes
        ```

## Exercice 2 

!!! exo 
    === "Enoncé"
        Recopier et compléter sous Python la fonction suivante en respectant la spécification. On ne recopiera pas les commentaires.

        ```python linenums='1'
        def dichotomie(tab, x):
            """
            tab : tableau d’entiers trié dans l’ordre croissant
            x : nombre entier
            La fonction renvoie True si tab contient x et False sinon
            """
            debut = ...
            fin = ...
            while debut <= fin:
                milieu = ...
                if x == tab[milieu]:
                    return ...
                if x > ...:
                    debut = ...
                else:
                    fin = ...
            return ...

        ```

        Exemples :
        ```python
        >>> dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],28)
        True
        >>> dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],27)
        False
        ```

    === "Solution" 
        ```python linenums="1" hl_lines="7 8 10 12 13  14 16 17"
        def dichotomie(tab, x):
            """
            tab : tableau d’entiers trié dans l’ordre croissant
            x : nombre entier
            La fonction renvoie True si tab contient x et False sinon
            """
            debut = 0
            fin = len(tab) - 1
            while debut <= fin:
                milieu = (debut + fin) // 2
                if x == tab[milieu]:
                    return True
                if x > tab[milieu]:
                    debut = milieu + 1
                else:
                    fin = milieu - 1
            return False
        ```