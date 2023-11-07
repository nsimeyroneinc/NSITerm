hide: - navigation  in docs.md

{% set repere_sujet = "22-NSIJ1LR1" %}

{{ corrige_sujetbac(repere_sujet) }}


{{ corrige_exobac(repere_sujet,1) }}

1.  a. Le `1` est défilé et enfilé 
    {{ file([1,4,3,8,2]) }} 
    b. Le `5` est dépilé et empiler (la pile reste donc dans l'état où elle se trouvait)
    {{ pile([2, 6, 8, 5]) }} 
    c. Le `5` est dépilé de `p` et enfilé dans `f` puis le `8` est dépilé de `p` et enfilé dans `f`.
    {{ file([8, 5, 4, 3, 8, 2, 1])}} <br>
    {{ pile([2, 6])}} 
    d. Le `1` est défiler de `f` et empiler dans `p` puis le `2` est dépilé de `f`empilé dans `p`.
    {{ file([4,3,8])}} <br>
    {{ pile([2,6,8,5,1,2])}}

    !!! bug
        A la question suivante, l'énoncé indique que la fonction `mystere` modifie la file mais *ne renvoie rien*. Cependant, on trouve  à la fin du code de `mystere` un return `p`. Cette fonction renvoie donc une pile (qui comme nous le verrons est vide)

2.  Avant le premier passage `f` contient {{ file([1,2,3,4]) }}
Puis,les états  de la file `f` lors des passages successifs dans la première boucle `while` seront :
    - Tour 1 : `f` contient {{ file([1,2,3])}}
    - Tour 2 : `f` contient {{ file([1,2])}}
    - Tour 3 : `f` contient {{ file([1])}}
    A la fin de cette première boucle, les éléments de `f` sont empilés dans `p` qui contient alors :
    {{ pile([4,3,2,1]) }}
    Dans la deuxième boucle `while` on dépile les éléments de `p` et on les enfile dans `f` :
    - Tour 1 `f` contient {{ file([1])}}
    - Tour 2 `f` contient {{ file([2,1])}}
    - Tour 3 `f` contient {{ file([3,2,1])}}
    - Tour 4 `f` contient {{ file([4,3,2,1])}}
    A la fin de la seconde boucle `while` la pile `p` est vide, cette fonction renvoie donc une pile vide.
 
3.  a.
    <table>
    <tr> 
    <td> <pre>f</pre> </td>
    <td> {{file([2,1,3])}} </td>
    <td> {{file([2,1])}}</td>
    <td> {{file([3,2])}}</td>
    <td> {{file([3])}}</td>
    <td> {{file([3])}}</td>
    <td> {{file([2,3])}}</td>
    <td> {{file([1,2,3])}}</td>
    </tr> 
    <tr> 
    <td style="vertical-align:middle"> <pre>p</pre> </td>
    <td style="vertical-align:bottom"> {{pile([])}} </td>
    <td style="vertical-align:bottom"> {{pile([3])}}</td>
    <td style="vertical-align:bottom"> {{pile([1])}}</td>
    <td style="vertical-align:bottom"> {{pile([1])}}</td>
    <td style="vertical-align:bottom"> {{pile([1,2])}}</td>
    <td style="vertical-align:bottom"> {{pile([1])}}</td>
    <td style="vertical-align:bottom"> {{pile([])}} </td>
    </tr>
    </table>

    b.

    !!! bug
        Cette algorithme semble conçu pour trier les éléments de la file mais ne fonctionne pas en l'état. En effet, la fonction `knuth` semble vouloir à chaque tour de la boucle `for`, avoir une pile `p` triée. Pour cela, les éléments de `p` supérieurs au nouvel élément à empiler `e` devraient être stockées dans une pile temporaire `p_temp`, ici ces éléments sont  enfilés dans la file à trier `f`.


{{ corrige_exobac(repere_sujet,2) }}

1.  a. On augmente l'indice `i` sans dépasser la longueur de la liste `Mousse` tant qu'on ne trouve pas `None` :
    ```python linenums="1" hl_lines="10 11"
    def donnePremierIndiceLibre(Mousse):
        """
        Mousse est une liste.
        La fonction doit renvoyer l’indice du premier
        emplacement libre (contenant None) dans la liste Mousse
        ou renvoyer 6 en l’absence d’un emplacement libre dans
        Mousse.
        """
        i = 0
        while i < len(Mousse) and Mousse[i] != None :
            i = i + 1
        return i
    ```

    b.  Si un indice libre existe alors on place `B` à cet indice dans `Mousse` :
    ```python linenums="1"
    def placeBulle(B):
        libre = donnePremierIndiceLibre(Mousse)
        if libre < len(Mousse):
            Mousse[libre] = B
    ```

2. Les deux bulles sont en contacts si la distance les séparant est inférieur à la somme de leurs rayons.
```python linenums="1"
def bullesEnContact(B1,B2):
    return distanceEntreBulles(B1,B2) <= B1.rayon + B2. rayon
```

    !!! aide
        Le code ci-dessus est équivalent à :
        ```python linenums="1"
            def bullesEnContact(B1,B2):
            if distanceEntreBulles(B1,B2) <= B1.rayon + B2:
                return True
            else:
                return False
        ```


3.  A la ligne 10, on indique que la surface de la nouvelle bulle est la somme des surfaces des deux bulles entrant en collision. Les lignes 13 et 14 divisent par 2 les deux composantes de la vitesse. Et enfin ligne 16, la petite bulle disparait donc la valeur de l'indice qu'elle occupait devient `None`
```python linenums="1" hl_lines="10 13 14 16"
def collision(indPetite, indGrosse, Mousse) :
    """
    Absorption de la plus petite bulle d’indice indPetite
    par la plus grosse bulle d’indice indGrosse. Aucun test
    n’est réalisé sur les positions.
    """
    # calcul du nouveau rayon de la grosse bulle
    surfPetite = pi*Mousse[indPetite].rayon**2
    surfGrosse = pi*Mousse[indGrosse].rayon**2
    surfGrosseApresCollision = surfPetite + surfGrosse
    rayonGrosseApresCollision = sqrt(surfGrosseApresCollision/pi)
    #réduction de 50% de la vitesse de la grosse bulle
    Mousse[indGrosse].dirx = Mousse[indGrosse].dirx/2
    Mousse[indGrosse].diry = Mousse[indGrosse].diry/2
    #suppression de la petite bulle dans Mousse
    Mousse[indPetite] = None
```

    !!! aide
        On rappelle que la surface d'un disque de rayon $r$ est $\pi\,r^2$

    !!! bug
        * Le rayon de la grosse bulle est modifié lors d'une collision, on devrait donc trouver dans le code de la fonction `collision` la ligne `Mousse[indGrosse].rayon = rayonGrosseApresCollision`.
        * Dans les paramètres d'appel `mousse` est en minuscule dans l'énoncé.
        * Des espaces superflus figurent dans l'énoncé (par exemple entre `Mousse` et `[indPetite]`), on les a supprimé dans la correction pour respecter la notation usuelle de Python.

{{ corrige_exobac(repere_sujet,3) }}

1.  a. Cette requête retourne les `titre` de la table `qcm` dont la date est après le 10/01/2022. C'est à dire :

    | titre |
    |-------|
    | {{sc("poo")}} |
    | Arbre Parcours |

    b.
    ```sql
    SELECT note FROM lien_eleve_qcm WHERE ideleve = 4;
    ```

2.  a. Le couple `(ideleve,idqcm)` est la clé primaire de la table `lien_eleve_qcm`, or une clé primaire est *unique* et donc deux enregistrements dans cette table ne peuvent avoir les mêmes valeurs pour le couple `(ideleve,idqcm)` c'est à dire qu'un même élève ne peut pas avoir fait deux fois le même qcm.

    b. La table `lien_eleve_qcm` est modifiée, on doit y ajouter l'enregistremen `(4,2,18)` car l'`ideleve` de *Marty Mael* est 4, qu'il a fait le `qcm` d'`idqcm` 2 et qu'il a eu la note de 18.

    c. 
    ```sql
    INSERT INTO eleves VALUES (6,"Lefèvre","Kevin")
    ```

    d. 
    ```sql
    DELETE FROM lien_eleve_qcm WHERE ideleve=2
    ```

3.  a.
    ```sql
    SELECT nom, prenom FROM eleves
    JOIN lien_eleve_qcm ON eleves.ideleve = lien_eleve_qcm.ideleve
    WHERE idqcm = 4
    ```

    b. Le résultat de cette requête sera :

    | nom  | prenom |
    |------|--------|
    |Marty |Mael    |
    |Bikila|Abebe   |

    !!! note
        On a supposé l'élève Dubois Thomas ne figure plus dans la base suite à la requête de la question 2.d. Dans le cas contraire, il faudrait le rajouter au résultat précédent.

4.
```sql
SELECT eleves.nom, eleves.prenom, lien_eleve_qcm.note FROM eleves
JOIN lien_eleve_qcm ON eleves.ideleve = lien_eleve_qcm.ideleve
JOIN qcm ON qcm.idqcm = lien_eleve_qcm.idqcm
WHERE qcm.titre = "Arbre Binaire"
```

{{ corrige_exobac(repere_sujet,4) }}

1.  
    a. Un arbre binaire est un arbre d'arité 2, c'est à dire un arbre dans lequel chaque noeud possède au plus deux fils. C'est bien le cas ici, une personne   ayant au maximum deux parents connus.

    b. Dans un arbre binaire de recherche, on dispose d'une relation d'ordre entre les clés associées à chaque noeud et pour tout noeud, sa clé est supérieure aux  clés du sous arbre gauche et inférieure aux clés du sous arbre droit. Ici les clés sont des personnes sur lesquelles on n'a pas de relation d'ordre.

2.  a. On rappelle que dans un parcours en *profondeur préfixe*, on liste en premier la racine puis récursivement les clés du sous arbre gauche et du sous arbre droit. Ce qui donne ici :  
    Albert Normand :octicons-dash-16: Jules Normand :octicons-dash-16: Michel Normand :octicons-dash-16: Jules Normand :octicons-dash-16: Odile Picard :octicons-dash-16: Hélène Breton  :octicons-dash-16: Evariste Breton

    b. Dans le parcours en *profondeur infixe*, on liste récursivement les clés du {{sc("sag")}} puis la racine puis les clés du {{sc("sad")}}. Ce qui donne ici :
    Jules Normand :octicons-dash-16: Michel Normand :octicons-dash-16: Odile Picard :octicons-dash-16: Jules Normand :octicons-dash-16: Evariste Breton :octicons-dash-16: Hélène Breton :octicons-dash-16: Camélia Charentais

    c. En parcours **prefixe** on insère l'affichage du tuple `(prenom,nom)` **avant** de relancer les parcours récursifs sur les deux sous arbres.
    ```python
    def parcours(racine_de_l_arbre) :
        if racine_de_l_arbre != None :
        noeud_actuel = racine_de_l_arbre
        print(noeud_actuel.identite)
        parcours(noeud_actuel.gauche)
        parcours(noeud_actuel.droite)
    ```

    d. En parcours **infixe** on insère l'affichage du tuple `(prenom,nom)` **entre**  les parcours récursifs sur les deux sous arbres.
    ```python
    def parcours(racine_de_l_arbre) :
        if racine_de_l_arbre != None :
        noeud_actuel = racine_de_l_arbre
        parcours(noeud_actuel.gauche)
        print(noeud_actuel.identite)
        parcours(noeud_actuel.droite)
    ```

3.  a. 
    ```python
    class Noeud() :
        def __init__(self, prenom, nom) :
            self.identite = (prenom, nom)
            self.gauche = None
            self.droite = None
            self.generation = 0
    ```

    !!! bug
        Dans l'énoncé, `self`  ne figure pas dans les paramètres de `__init__` (ajouté dans cette correction)

    
    b. 
    ```python
    def numerotation(racine_de_l_arbre, num_gen=0) :
        if racine_de_l_arbre != None:
            racine_de_l_arbre.generation = num_gen
            numerotation(racine_de_l_arbre.gauche,num_gen+1)
            numerotation(racine_de_l_arbre.droit,num_gen+1)
    ```

4.  Cette fonction parcourt l'arbre en préfixe mais affiche seulement les noeuds droit, ce qui donne :
Odile Picard :octicons-dash-16: Hélène Breton :octicons-dash-16: Camélia Charentais :octicons-dash-16: Marie Comtois :octicons-dash-16: Eulalie Lorrain :octicons-dash-16: Gabrielle Savoyard :octicons-dash-16: Janet Chesterfield 

{{ corrige_exobac(repere_sujet,5) }}

1.  a. Un adresse IPv4 se compose de 4 octects.

    b. Le PC3 a pour adresse  IPv4 : 172.150.4.30/24 le masque de sous réseau est donc 11111111.11111111.11111111.00000000 c'est à dire 255.255.255.0

2. Tableau complété :
![tableau complété](../../images/Corriges/22-NSIJ1LR1-1.png){.imgcentre}

    !!! aide
        * Exemple de la conversion binaire décimal : $150=${{binaire("10010110")}}
        * On rappelle qu'un & logique vaut 1 uniquement lorsque les deux entrées valent 1.

3.  a. L'adresse `172.150.10.257` n'est pas valide (le dernier chiffre n'est pas entre `0` et `255`). L'adresse `172.154.4.30` ne fait pas partie du réseau (ne commence pas par `172.150.4`) L'adresse `172.150.4.0` est celle du réseau. Et enfin, * `172.150.4.10`
 est déjà utilisée. Pour un nouvelle ordinateur on peut donc utiliser :

    * `172.150.4.11`
    * `172.150.4.200`

    b. Pour connaître l'adresse IP, on peut utiliser la commande `ifconfig` (système Linux) ou `ipconfig` (Windows).

4. Les machines sont sur des réseaux différents (`172.16.1.10\16` d'un côté et `192.168.5.10\16` de l'autre) un switch ne permet donc pas de les relier. Pour que cela fonctionne, il faudrait changer la configuration de toutes les machines d'un des sous réseau.
L'alternative est d'utiliser un *routeur* qui permet d'interconnecter les deux sous réseau en conservant leur configuration.

5. 
```python
def adresse(adresse,liste_ip):
    if adresse not in liste_ip:
        liste_ip.append(adresse)
        print("pas trouvée, ajoutée")
    else:
        print("trouvée")
```