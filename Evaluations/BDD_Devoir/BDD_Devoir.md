---
title : Thème 4 - Base de données
subtitle: Langage SQL - Devoir 01
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

SQL : Devoir n°1
===

<table  class="yellowTable">
        <tr >
            <th  class="yellowTh";width="100%"; style="text-align:center;border:none;font-size:15pt;">Thème 2 : Base de données</th>
        </tr>
</table>
<br>

<table  class="yellowTable">
        <tr >
            <th width="20%"; style="background-color: #3B444B;color:white;text-align:center;border:none;font-size:40pt;">
            Eval.
            </th>
            <th  class="yellowTh";width="80%"; style="text-align:center;border:none;font-size:25pt;">Langage SQL</th>
        </tr>
</table>
<br>



## D'après 2021, France, J2, 

L'énoncé de cet exercice utilise les mots du langage SQL suivants :
`SELECT FROM, WHERE, JOIN ON, INSERT INTO VALUES, UPDATE, SET, DELETE,
COUNT, AND, OR`.  
On considère dans cet exercice une gestion simplifiée des emprunts des ouvrages d'un CDI. La base de données utilisée sera constituée de trois relations (ou tables) nommées `Eleves`, `Livres` et `Emprunts` selon le schéma relationnel suivant :  

* {{ relation("Livres", "isbn (CHAR 13)", "titre (CHAR)", "auteur (CHAR)") }}  
* {{ relation("Emprunts", "idEmprunt (INT)", "#idEleve (INT)", "#isbn (CHAR 13)", "dateEmprunt (DATE)", "dateRetour (Date)") }}  
* {{ relation("Eleves", "idEleve (INT)", "nom (CHAR)", "prenom (CHAR)", "classe (CHAR)") }}  


Dans ce schéma relationnel, un attribut souligné indique qu'il s'agit d'une clé primaire.  

Le symbole # devant un attribut indique qu'il s'agit d'une clé étrangère. Ainsi, l'attribut `idEleve` de la relation `Emprunts` est une clé étrangère qui fait référence à la clé primaire `idEleve` de la relation `Eleves`. De même l'attribut `isbn` de la relation `Emprunts` est une clé étrangère qui fait référence à la clé primaire `isbn` de la relationcompléter `Livres`.  


**1.** Expliquer pourquoi le code `SQL` ci-dessous provoque une erreur.  

```SQL
INSERT INTO Eleves VALUES (128, 'Dupont', 'Jean', 'T1') ;
INSERT INTO Eleves VALUES (200, 'Dupont', 'Jean', 'T1') ;
INSERT INTO Eleves VALUES (128, 'Dubois', 'Jean', 'T2') ;
```



**2.** Dans la définition de la relation `Emprunts`, qu'est-ce qui assure qu'on ne peut pas enregistrer un emprunt pour un élève qui n'a pas encore été inscrit dans la relation `Eleves` ?


**3.** Écrire une requête `SQL` qui renvoie les titres des ouvrages de Molière détenus par le CDI.



**4.** Décrire le résultat renvoyé par la requête ci-dessous.

```SQL
SELECT COUNT(*)
FROM Eleves
WHERE classe = 'T2' ;
```



**5.** Camille a emprunté le livre « *Les misérables* ». Le code ci-dessous a permis
d'enregistrer cet emprunt.

```SQL
INSERT INTO Emprunts
VALUES (640, 192, '9782070409228', '2020-09-15', NULL);
```

Camille a restitué le livre le 30 septembre 2020.
Recopier et compléter la requête ci-dessous de manière à mettre à jour la date
de retour dans la base de données.

```SQL
UPDATE Emprunts 
SET ........................ 
WHERE ........................ ;
```



**6.** Décrire le résultat renvoyé par la requête ci-dessous.

```SQL
SELECT DISTINCT nom, prenom
FROM Eleves, Emprunts
WHERE Eleves.idEleve = Emprunts.idEleve
AND Eleves.classe = 'T2' ;
```


**7.** Écrire une requête SQL qui permet de lister les noms et prénoms des élèves qui
ont emprunté le livre « *Les misérables* ».

