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
            05
            </th>
            <th  class="yellowTh";width="80%"; style="text-align:center;border:none;font-size:25pt;">Epreuve Pratique</th>
        </tr>
</table>
<br>


## Exercice 1 

!!! exo 

Programmer la fonction ```moyenne```   prenant en paramètre un tableau d'entiers ```tab```   (type `list`) qui renvoie la moyenne de ses éléments si le tableau est non vide et affiche 'erreur' si le tableau est vide.

Exemples :
```python
>>> moyenne([5,3,8])
5.333333333333333
>>> moyenne([1,2,3,4,5,6,7,8,9,10])
5.5
>>> moyenne([])
'erreur'
```

## Exercice 2

!!! exo
On considère un tableau d'entiers `tab` (type `list` dont les éléments sont des `0` ou des `1`). On se propose de trier ce tableau selon l'algorithme suivant : à chaque étape du tri,le tableau est constitué de trois zones consécutives, la première ne contenant que des `0`,
la seconde n'étant pas triée et la dernière ne contenant que des `1`.

<table>
<tr>
<td>Zone de 0</td><td>Zone non triée</td><td>Zone de 1</td>
</tr>
</table>

Tant que la zone non triée n'est pas réduite à un seul élément, on regarde son premier
élément :

- si cet élément vaut 0, on considère qu'il appartient désormais à la zone ne contenant que des 0 ;  
- si cet élément vaut 1, il est échangé avec le dernier élément de la zone non triée et on considère alors qu’il appartient à la zone ne contenant que des 1.  

Dans tous les cas, la longueur de la zone non triée diminue de 1.

Recopier sous Python en la complétant la fonction `tri` suivante :

```python linenums='1'
def tri(tab):
    #i est le premier indice de la zone non triee, j le dernier indice.
    #Au debut, la zone non triee est le tableau entier.
    i = ...
    j = ...
    while i != j :
        if tab[i]== 0:
            i = ...
        else :
            valeur = tab[j]
            tab[j] = ...
            ...
            j = ...
    ...
```

Exemple :

```python
>>> tri([0,1,0,1,0,1,0,1,0])
[0, 0, 0, 0, 0, 1, 1, 1, 1]       
```