hide: - navigation  in docs.md

{% set repere_sujet = "23-NSIJ2PO1" %}

{{ corrige_sujetbac(repere_sujet) }}


{{ corrige_exobac(repere_sujet,1) }}

1. 
    a. Cet arbre est un arbre binaire car chaque nœud possède au plus deux ﬁls.

    b. L’arbre ci-dessus n’est pas un arbre binaire de recherche car par exemple la valeur du nœud 4 est le ﬁls droit de la racine dont la valeur est 13. 
    Dans un arbre binaire de recherche chaque nœud du sous-arbre gauche a une valeur inférieure ou égale à celle du nœud considéré et chaque nœud du sous-arbre droit à une valeur supérieure ou égale à celle du nœud considéré.
    
2.  a. 
    ```python
    assert isinstance(mini, int) and isinstance(maxi, int) and mini <= maxi
    ```

    b. 
    ```mermaid
    graph TD
        A("construire(0,8)") --> B("construire(0,4)") 
        B --> D("construire(0,2)")
        B --> E("construire(2,4)")
        A --> H("construire(4,8)")
        H --> I("construire(4,6)")  
        H --> J("construire(6,8)")
    ```
    c. 
    ```mermaid
    graph TD
        A(3) --> B(2) 
        B --> D(1)
        B --> E(1)
        A --> C(4)
        C --> F(3)
        C --> G(7)
    ```

    d. 
    ```mermaid
    graph TD
        A(1) --> B(0) 
        A --> D(2)
    ```

    e. Le parcours inﬁxe de l’arbre binaire obtenu dans la question 2.c est :  
    1, 2, 3, 4, 5, 6, 7  
    C’est un arbre binaire de recherche car le parcours inﬁxe parcours les valeurs des nœuds dans l’ordre croissant  

    f.
    ```python linenums='1' hl_lines='5 7'
    def maximum(abr):
        if abr is None:
            return None
        elif abr.droit is None:
            return abr.valeur
        else:
            return maximun(abr.droit)
    ```    
2.  a. 
    ```python
    >>> mystere(abr_7_noeuds, 5, [])
    [6, 4, 5]
    >>> mystere(abr_7_noeuds, 6, [])
    [6]
    >>> mystere(abr_7_noeuds, 2, [])
    []
    ```

    b. La fonction `mystere` permet de déterminer le chemin vers la valeur x entrée en paramètre en partant de la racine de l’arbre si elle existe. Si la valeur x n’est pas dans l’arbre binaire de recherche, cette fonction renvoie une liste vide.

  
    ```

{{ corrige_exobac(repere_sujet,2) }}

1.  a. L’appareil à raclette a pour id 4. Dans la table Possede, les membres d’id 1 et 2, c’est-à-dire Ali Mohamed et Alonso Fernando, proposent à la location un  appareil à raclette.

    b. Dans la table Possede, le membre d’id 5 n’est pas présent. Cela signiﬁe qu’il ne propose pas d’objet à la location. Ce membre est Kane Harry.


2.  a. Cette requête renvoie :  
    Dupont Antoine  
    Kane Harry  
    

    b. 
    ```sql
    SELECT tarif 
    FROM Objet 
    WHERE description = "Scie circulaire" ;
    ```

    c. 
    ```sql      
    UPDATE Objet
    SET tarif = 15
    WHERE description ="Nettoyeur haute pression" ;
    ```

    d. 
    ```sql
    INSERT INTO Membre VALUES (6, "Renard", "Wendie", "69100");
    ```

3.  a. Si ce couple était utilisé comme clé primaire, un membre ne pourrait réserver qu’une seul fois un même objet

    b. Ce membre est également présent dans les tables Possede et Reservation. Son attribut id_membre est clé étrangère de ces tables. Il faut donc d’abord supprimer ces entités des tables Possede et Reservation avant de pouvoir le supprimer de la table Membre.

    c.
    ```sql
    DELETE FROM Possede WHERE id_membre = 1;
    DELETE FROM Reservation WHERE id_membre = 1;
    ```

4.  a. 
    ```sql
    SELECT COUNT(*) FROM Reservation
    JOIN Membre ON Membre.id_membre = Reservation.id_membre
    WHERE Membre.nom = "Alfonso" AND Membre.prenom = "Fernando";
    ```

    b. 
    ```sql
    SELECT nom, prenom FROM Membre
    JOIN Possede ON Possede.id_membre = Objet.id_membre
    JOIN Objet ON Objet.id_objet = Possede.id_objet
    WHERE Objet.description = "Appareil à raclette";
    ```


{{ corrige_exobac(repere_sujet,3) }}

1.  a. 
    ```mermaid
    graph TD
        A("9617") --> B("9794") 
        A --> D("9750")
        A --> E("9697")
        A --> H("9657")
        B --> I("9795")
    ```
    b. La commande qui a lancé le premier processus de firefox est bash.

    c. La commande permettant de supprimer tous les processus liés à firefox est kill 9617.


2.  a. 
    ![](data/23-NSIJ2PO1-ex3.png){width:50%}

    b. Les temps d’exécution des quatre processus sont :

    | Processus|Instant d’arrivée |Instant de terminaison | Temps d’exécution| 
    | :---:| :---:| :---:| :---:|
    | 1| 0| 12| $12-0=12$| 
    | 2| 2| 18| $18-2=16$| 
    | 3| 3| 5| $5-3=2$| 
    | 4| 7| 9| $9-7=2$| 

    On obtient le temps d’exécution moyen : $\dfrac{12+16+2+2}{4}=8$

    c. P1-P1-P1-P1-P3-P3-P1-P1-P1-P1-P4-P4-P2-P2-P2-P2-P2-P2

    d. Les temps d’exécution des quatre processus sont :

    | Processus|Instant d’arrivée |Instant de terminaison | Temps d’exécution| 
    | :---:| :---:| :---:| :---:|
    | 1| 0| 10| $10-0=10$| 
    | 2| 2| 18| $18-2=16$| 
    | 3| 3| 6| $6-3=3$| 
    | 4| 7| 12| $10-7=5$| 

    On obtient le temps d’exécution moyen : $\dfrac{10+16+3+5}{4}=8.5$  
    Cet ordonnancement est moins performant que le précédent.


3.  a. 
    ```python linenums='1' hl_lines='7 8 9 10 11'
    def choix_processus(liste_attente):
    """Renvoie l'indice du processus le plus court parmi 
    ceux présents en liste d'attente liste_attente"""
        if liste_attente != []:
            mini = len(liste_attente[0])
            indice = 0
            # On parcourt les processus dans la liste d'attente
            for i in range(1, len(liste_attente)):
                # Si on trouve un processus plus court
                if len(liste_attente[i]) < mini:
                    indice = i # On retient son indice
                    mini = len(liste_attente[i])
            return indice
    ```

    b.
    ```python linenums='1' hl_lines='7 8 9 10 11'
    def ordonnancement(liste_proc):
        """Exécute l'algorithme d'ordonnancement
        liste_proc -- liste des processus
        Renvoie la liste d'exécution des processus"""
        execution = []
        attente = scrutation(liste_proc, [])
        while attente != []:
            indice = choix_processus(attente)
            # Retrait de la liste d'attente du dernier élément du
            # processus le plus court
            process_execute = attente[indice].pop()
            # Le processus est entièrement fini, il est enlevé de la
            # liste d'attente
            if attente[indice] == []:
                attente.pop(indice)
                # On ajoute l'élément du processus choisi à la liste
                # d'exécution
            execution.append(process_execute)
            attente = scrutation(liste_proc, attente)
        return execution
    ```
