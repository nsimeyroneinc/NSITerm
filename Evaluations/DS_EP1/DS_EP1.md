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
            01
            </th>
            <th  class="yellowTh";width="80%"; style="text-align:center;border:none;font-size:25pt;">Epreuve Pratique</th>
        </tr>
</table>
<br>


## Exercice 1 

!!! exo 
    === "Enoncé"
        Écrire une fonction `tri_selection` qui prend en paramètre une liste `tab` de nombres entiers et qui trie ce tableau en place (c'est-à-dire que le tableau est modifié) par ordre croissant.

        On utilisera l’algorithme suivant :

        - on parcours le tableau de gauche à droite :  
            - on recherche le minimum du tableau entre cette position courante et la fin du tableau.
            - on échange alors les 2 valeurs.


        Exemple :
        ```python
        >>> tab = [1, 52, 6, -9, 12]
        >>> tri_selection(tab)
        >>> tab
        [-9, 1, 6, 12, 52]
        >>> tab_vide = []
        >>> tri_selection(tab_vide)
        >>> tab_vide
        []
        ```
    === "Solution"
        ```python
        def tri_selection(tab):
            for i in range(len(tab)-1):
                indice_min = i
                for j in range(i+1, len(tab)):
                    if tab[j] < tab[indice_min]:
                        indice_min = j
                tab[i], tab[indice_min] = tab[indice_min], tab[i]
            return tab
        ```

## Exercice 2 

!!! exo 
    === "Enoncé"

        Chaque soir, les auditeurs d’une radio votent en ligne pour leur artiste favori. Ces votes sont stockés dans un tableau.

        Exemple :

        ```python
        Urne = ['Oreilles sales', 'Oreilles sales', 'Oreilles sales', 'Extra Vomit',
        'Lady Baba', 'Extra Vomit', 'Lady Baba', 'Extra Vomit', 'Lady Baba', 'Extra Vomit']
        ```

        La fonction depouille doit permettre de compter le nombre de votes exprimés pour chaque artiste. Elle prend en paramètre un tableau et renvoie le résultat dans un dictionnaire dont les clés sont les noms des artistes et les valeurs le nombre de votes en leur faveur.

        La fonction vainqueur doit désigner le nom du ou des gagnants. Elle prend en paramètre un dictionnaire dont la structure est celle du dictionnaire renvoyé par la fonction depouille et renvoie un tableau. Ce tableau peut donc contenir plusieurs éléments s’il y a des artistes ex- aequo.

        Compléter les fonctions depouille et vainqueur ci-après pour qu’elles renvoient les résultats attendus.

        ```python
        urne = ['Oreilles sales', 'Oreilles sales', 'Oreilles sales',
            'Extra Vomit', 'Lady Baba', 'Extra Vomit', 'Lady Baba',
            'Extra Vomit', 'Lady Baba', 'Extra Vomit']

        def depouille(urne):
            resultat = ...
            for bulletin in urne:
                if ...:
                    resultat[bulletin] = ...
                else:
                    ...
            return resultat

        def vainqueur(election):
            nmax = 0
            for candidat in election:
                if ... > ... :
                    nmax = ...
            liste_finale = [nom for nom in election if election[nom] == ...]
            return ...
        ```

    === "Solution"
        ```python linenums="1" hl_lines="2 4 5 7 13 14 15 16"
        def depouille(urne):
            resultat = {}
            for bulletin in urne:
                if bulletin in resultat:
                    resultat[bulletin] = resultat[bulletin] + 1
                else:
                    resultat[bulletin] = 1
            return resultat

        def vainqueur(election):
            nmax = 0
            for candidat in election:
                if election[candidat] > nmax:
                    nmax = election[candidat]
            liste_finale = [nom for nom in election if election[nom] == nmax]
            return liste_finale
        ```