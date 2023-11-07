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
            07
            </th>
            <th  class="yellowTh";width="80%"; style="text-align:center;border:none;font-size:25pt;">Epreuve Pratique</th>
        </tr>
</table>
<br>


## Exercice 1 

!!! exo 

Écrire une fonction `maxi` qui prend en paramètre une liste `tab` de nombres entiers et renvoie un couple donnant le plus grand élément de cette liste, ainsi que l’indice de la première apparition de ce maximum dans la liste.

Exemple :
```python
>>> maxi([1,5,6,9,1,2,3,7,9,8])
(9,3)
```


## Exercice 2

!!! exo

La fonction `recherche` prend en paramètres deux chaines de caractères `gene` et `seq_adn` et renvoie `True` si on retrouve `gene` dans `seq_adn` et `False` sinon.  
Compléter le code Python ci-dessous pour qu’il implémente la fonction `recherche`.  

```python linenums='1'
def recherche(gene, seq_adn):
    n = len(seq_adn)
    g = len(gene)
    i = ...
    trouve = False
    while i < ... and trouve == ... :
        j = 0
        while j < g and gene[j] == seq_adn[i+j]:
            ...
        if j == g:
            trouve = True
        ...
    return trouve
```

Exemples :

```python
>>> recherche("AATC", "GTACAAATCTTGCC")
True
>>> recherche("AGTC", "GTACAAATCTTGCC")
False
```