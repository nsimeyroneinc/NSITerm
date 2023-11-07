
{% set num = 4 %}
{% set titre = "Les tris - Dichotomie - Diviser pour régner" %}
{% set theme = "devoir" %}
{% set niveau = "terminale" %}


{{ titre_chapitre(num,titre,theme,niveau)}}

{{ initexo(0) }}



## Q.C.M.

!!! exo QCM

{{qcm_chapitre_devoir(num)}}

## D'aprés exercice BAC

!!! exo 
### Partie A : Généralités - Cours 

!!! fabquestion "Question A.1"
    Quel est l’ordre de grandeur du coût, en nombre de comparaisons, de l’algorithme de tri fusion pour une liste de longueur $n$ ?  

??? success "Réponse"
       $O(nlog_2(n))$  



!!! fabquestion "Question A.2"   
    Citer le nom d’un autre algorithme de tri. Donner l’ordre de grandeur de son coût, en nombre de comparaisons, pour une liste de longueur .  
    Comparer ce coût à celui du tri fusion.   

??? success "Réponse"
    L’algorithme de tri par insertion a une complexité en temps dans le pire des cas en $O(n^2)$.  
    L’algorithme du tri par insertion est moins efficace que l’algorithme de tri fusion.  


### Partie B : Tri fusion


L’algorithme de tri fusion utilise deux fonctions `moitie_gauche` et `moitie_droite` qui prennent en argument une liste L et renvoient respectivement : 

 - la sous-liste de L formée des éléments d’indice strictement inférieur à `len(L)//2` ;  
 - la sous-liste de L formée des éléments d’indice supérieur ou égal à `len(L)//2`.  

On rappelle que la syntaxe a//b désigne la division entière de a par b.  

Par exemple,
```python
>>> L = [3, 5, 2, 7, 1, 9, 0]
>>> moitie_gauche(L)
[3, 5, 2]
>>> moitie_droite(L)
[7, 1, 9, 0]
>>> M = [4, 1, 11, 7]
>>> moitie_gauche(M)
[4, 1]
>>> moitie_droite(M)
[11, 7]
```

L’algorithme utilise aussi une fonction `fusion` qui prend en argument deux listes triées `L1` et `L2` et renvoie une liste `L` triée et composée des éléments de `L1` et `L2`.  
On donne ci-dessous le code python d’une fonction récursive `tri_fusion` qui prend en argument une liste `L` et renvoie une nouvelle liste triée formée des éléments de `L`.

```python
def tri_fusion(L):
	n = len(L)
	if n<=1 :
		return L
	print(L)
	mg = moitie_gauche(L)
	md = moitie_droite(L)
	L1 = tri_fusion(mg)
	L2 = tri_fusion(md)
	return fusion(L1, L2)
```

!!! fabquestion "Question B.1"
    Donner la liste des affichages produits par l’appel suivant.  
	```python
	tri_fusion([9, 5, 3, 1, 7, 6, 10, 3])
	```

??? success "Réponse"
    ```python
    [9, 5, 3, 1, 7, 6, 10, 3]
    [9, 5, 3, 1]
    [9, 5]
    [3, 1]
    [7, 6, 10, 3]
    [7, 6]
    [10, 3]  
    ``` 


On s’intéresse désormais à différentes fonctions appelées par `tri_fusion`, à savoir `moitie_gauche` et `fusion`.  

!!! fabquestion "Question B.2"
    Écrire une fonction `moitie_gauche(tab)` qui prend en argument un tableau `tab` et renvoie un nouveau tableau contenant la moitié gauche de `tab`.

??? success "Réponse"
    ```python
    def moitie_gauche(L):
        n = len(L)
        fin = n//2
        tab = []
        for i in range(fin):
            tab.append(L[i])
        return tab
    ```

!!! fabquestion "Question B.3"
    On donne ci-dessous une version incomplète de la fonction `fusion`.  

    ```py linenums="1"
    def fusion(L1, L2):
        L = []
        n1 = len(L1)
        n2 = len(L2)
        i1 = 0
        i2 = 0
        while .... :
            if i1 >= n1:
                ...
                ...
            elif i2 >= n2:
                L.append(L1[i1])
                i1 = i1 + 1
            else:
                e1 = L1[i1]
                e2 = L2[i2]
                






        return L
    ```
    Dans cette fonction, les entiers i1 et i2 représentent respectivement les indices des éléments des listes L1 et L2 que l’on souhaite comparer :  

    - Si aucun des deux indices n’est valide, la boucle while est interrompue ;  
    - Si i1 n’est plus un indice valide, on va ajouter à L les éléments de L2 à partir de l’indice i2 ;  
    - Si i2 n’est plus un indice valide, on va ajouter à L les éléments de L1 à partir de l’indice i1 ;  
    - Sinon, le plus petit élément non encore traité est ajouté à L et on décale l’indice correspondant.  

    Écrire sur la copie les instructions manquantes de la ligne 7, des lignes 9 à 10 puis des lignes de 17 à 22.. 

??? success "Réponse"

    ```python linenums="1" hl_lines="7 9 10 17 18 19 20 21 22"
    def fusion(L1, L2):
        L=[]
        n1 = len(L1)
        n2 = len(L2)
        i1 = 0
        i2 = 0
        while i1<n1 or i2<n2:
            if i1>=n1:
                L.append(L2[i2])
                i2 = i2+1
            elif i2>=n2:
                L.append(L1[i1])
                i1=i1+1
            else :
                e1 = L1[i1]
                e2 = L2[i2]
                if e1 > e2:
                    L.append(e2)
                    i2 = i2 + 1
                else :
                    L.append(e1)
                    i1 = i1 + 1
        return L
    ```


### Partie C : Tri par insertion  

Le tri par insertion est un algorithme efficace qui s'inspire de la façon dont on peut trier une poignée de cartes. On commence avec une seule carte dans la main gauche (les autres cartes sont en tas sur la table) puis on pioche la carte suivante et on l'insère au bon endroit dans la main gauche.

!!! fabquestion "Question C.1"
	Voici une implémentation en Python de cet algorithme. Recopier et compléter les lignes 6 et 7 surlignées (uniquement celles-ci).
    ```py linenums="1"
    def tri_insertion(liste):
        """ trie par insertion la liste en paramètre """
        for indice_courant in range(1,len(liste)):
            element_a_inserer = liste[indice_courant]
            i = indice_courant - 1
            while i >= 0 and liste[i] > ................................ :
                liste[...........] = liste[...........]
                i = i - 1
                liste[i + 1] = element_a_inserer
    ```

??? success "Réponse"
    ```python
    def tri_insertion(liste):
    for indice_courant in range(1, len(liste)):
        element_a_inserer = liste[indice_courant]
        i = indice_courant - 1
        while i >= 0 and liste[i] > element_a_inserer:
            liste[i+1] = liste[i]
            i=i-1
        liste[i + 1] = element_a_inserer
    ```
    
On a écrit dans la console les instructions suivantes :
```python
notes = [8, 7, 18, 14, 12, 9, 17, 3]
tri_insertion(notes)
print(notes)
```
On a obtenu l'affichage suivant : 
```python
[3, 7, 8, 9, 12, 14, 17, 18]
```

On s'interroge sur ce qui s’est passé lors de l’exécution de `tri_insertion(notes)`.  

!!! fabquestion "Question C.2"
	Donner le contenu de la liste notes après le premier passage dans la boucle `for`.

??? success "Réponse"
    `Passage 1 : [7, 8, 18, 14, 12, 9, 17, 3]`

!!! fabquestion "Question C.3"
    Donner le contenu de la liste notes après le troisième passage dans la boucle `for`.

??? success "Réponse"
    `Passage 3 : [7, 8, 14, 18, 12, 9, 17, 3]`

!!! fabquestion "Question C.4"
    Donner le contenu de la liste notes étape par étape lors de l'éxecution de la fontion `tri_insertion`.

??? success "Réponse"

    ```python
    Passage 1 : [7, 8, 18, 14, 12, 9, 17, 3]
    Passage 2 : [7, 8, 18, 14, 12, 9, 17, 3]
    Passage 3 : [7, 8, 14, 18, 12, 9, 17, 3]
    Passage 4 : [7, 8, 12, 14, 18, 9, 17, 3]
    Passage 5 : [7, 8, 9, 12, 14, 18, 17, 3]
    Passage 6 : [7, 8, 9, 12, 14, 17, 18, 3]
    Passage 7 : [3, 7, 8, 9, 12, 14, 17, 18]
    ```