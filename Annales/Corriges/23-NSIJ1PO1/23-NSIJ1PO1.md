hide: - navigation  in docs.md

{% set repere_sujet = "23-NSIJ1PO1" %}

{{ corrige_sujetbac(repere_sujet) }}


{{ corrige_exobac(repere_sujet,1) }}

1. 
    a. La table contient déjà une entrée dont l'attribut id_equipe vaut 11. Comme il s'agit de la clé primaire cela provoque une erreur. C’est
la contrainte d’unicité

    b. L'attribut telephone est une chaine de caractère limité à 20. On ne pouvait pas choisir des entiers car les numeros de téléphone commençant par 0 il disparaitrait ainsi les espaces entre chaque paire de chiﬀres.

    c. 
    |Lyon | 451 cours d'Emile Zola,69100 Villeurbanne |04 05 06 07 08|
    
    d. La requête le nombre d'entrée dans la table `equipe`   
    Cette requête renvoie 12. Elle renvoie le nombre d’entités dans la relation Equipe.

    e. 
    ```sql
    SELECT nom
    FROM Equipe
    ORDER BY noms;
    ```

    f. 
    ```sql
    UPDATE Equipe
    SET nom='Tarbes'
    WHERE id_equipe=4;
    ```

2.  a. L'attribut `id_equipe` a été déclaré clé étrangère de la relation `Joueuse` pour référence à la clé primaire `id_equipe` de la table `Equipe`.  

    b. On ne peut pas supprimer directement l’équipe dans la relation Equipe car certaines entités de la relation Joueuse font référence à cette équipe : c’est la contrainte de référence.

    c. 
    ```sql
    SELECT Joueuse.nom, Joueuse.prenom
    FROM Joueuse
    JOIN Equipe ON Equipe.id_equipe=Joueuse.id_equipe
    WHERE Equipe.nom='Angers'
    ORDER BY Joueuse.nom;
    ```

3.  a. On peut proposer le schéma relationnel suivant : 
    {{relation("Match","id_match : INT", "date : DATE", "#id_equipe_domicile : INT", "#id_equipe_deplacement : INT","score_domicile : INT","score_deplacement : INT") }}
    
    \#id_equipe_domicile et #id_equipe_deplacement sont des clés étrangères qui font référence à la relation Equipe. 

    b.
    ```sql
    INSERT INTO Match VALUES (10, "23/10/2021", 3, 6, 73, 78) ;
    ```

4. a. On peut proposer le schéma relationnel suivant :
    {{ relation("Statistiques","id_stats : INT", "#id_joueuse : INT", "#id_match : INT","points : INT","passes_decisives : INT") }}

    b.
    ```sql
    SELECT Equipe.nom, Joueuse.nom, Joueuse.prenom, Statistiques.points, Statistiques.rebonds, Statistiques.passes_decisives
    FROM Statistiques
    JOIN Joueuse ON Joueuse.id_joueuse = Statistiques.id_joueuse
    JOIN Equipe ON Joueuse.id_equipe = Equipe.id_equipe
    WHERE Statistiques.id_match = 53 ;
    ```

{{ corrige_exobac(repere_sujet,2) }}

1.  a. 11 - 20 - 32 - 11 - 20 - 32 - 11 - 32 - 11  

    b. 11 - 11 - 20 - 20 - 32 - 32 - 11 - 11 - 32 

2.  a.
    ```python
    liste_attente=[Processus(11,4),Processus(20,2),Processus(32,3)]
    ```

    b. 
    ```python
    def execute_un_cycle(self):
        self.reste_a_faire-=1
        
    def change_etat(self,nouvel_etat):
        self.etat=nouvel_etat
        
    def est_termine(self):
        if self.reste_a_faire<=0:
            return True
        else:
            return False
    ```

    c. 
    ```python        
    def tourniquet(liste_attente, quantum):
        ordre_execution = []
        while liste_attente != []:
            # On extrait le premier processus
            processus = liste_attente.pop(0)
            processus.change_etat("En cours d'exécution")
            compteur_tourniquet = 0
            while processus.reste_a_faire > 0 and compteur_tourniquet < quantum :
                ordre_execution.append(processus.pid)
                processus.execute_un_cycle()
                compteur_tourniquet = compteur_tourniquet + 1
            if processus.reste_a_faire != 0:
                processus.change_etat("Suspendu")
                liste_attente.append(processus)
            else:
                processus.change_etat("Terminé")
        return ordre_execution
    ```

 

    

{{ corrige_exobac(repere_sujet,3) }}

1.  a. `from math import sqrt` permet d'import la fonction racine carrée de la bibliothèque math   
    b. Cette instruction renvoie une False à cause des erreurs d’arrondis sur les nombres à virgule ﬂottante. En eﬀet, les nombres à virgule ﬂottante sont représentés par une somme de puissance de 2. Comme 0,1, 0,2 et 0,3 ne peuvent pas s’exprimer comme une somme ﬁnie de puissance de 2, l’opération booléenne précédente renvoie False  
    c. `point_A` est un tuple qui n'est pas mutable d'où l'erreur.

2.  a. 
    ```python linenums='1' hl_lines='6'
    from math import sqrt
    class Segment:
        def __init__(self,point1,point2):
            self.p1=point1
            self.p2=point2
            self.longueur= sqrt((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)
    ```

    b.  
    ```python
    def liste_segments(liste_points):
        n = len(liste_points)
        segments = []
        for i in range(n-1):
            for j in range(i+1, n):
                # On construit le segment à partir des points i et j.
                seq = Segment(liste_points[i],liste_points[j])
                segments.append(seg) # On l'ajoute à la liste
        return segments    
    ```

    c. Pour liste de points de longueur n, on aura $(n-1) + (n-2) + ... + 1=(n-1) \times \dfrac{n-1+1}{2}= \dfrac{n \times (n-1)}{2}$ segments 

    d. La complexité est donc de l'ordre de $O(n^2)$.

3.  a. 
    ```python
    def plus_court_segment(liste_segments):
        if len(liste_segments)==1:
            return liste_segments[0]
        else:
            seg_gauche=plus_court_segment(moitie_gauche(liste_segments))
            seg_droite=plus_court_segment(moitie_droite(liste_segments))
        if seg_gauche.longueur>seg_droite.longueur:
            return seg_droite
        else:
            return seg_gauche
    ```

4.  a. 
    ```python
    point_A=(3,4)
    point_B=(2,3)
    point_C=(-3,-1)

    nuage_points=[point_A,point_B,point_C]
    ```

    b. 
    ```python
    segment=plus_court_segment(liste_segments(nuage_points))

    print((segment.p1[0],segment.p1[1]),(segment.p2[0],segment.p2[1]))
    ```
