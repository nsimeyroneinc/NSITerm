---
title : Thème 4 - Base de données
subtitle: Langage SQL
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

Langage SQL : Résumé
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
            02
            </th>
            <th  class="yellowTh";width="80%"; style="text-align:center;border:none;font-size:25pt;">Résumé cours : Langage SQL</th>
        </tr>
</table>
<br>
**Programme Terminale**  

|Contenus|Capacités attendues|Commentaires|
|:---:|:---:|:---:|
|Langage SQL : requête d'interrogation et de mise à jour d'une base de données| Identifier les composants d'une requête.  Construire des requêtes 'interrogation à l'aide des clauses du langage SQL :   ```SELECT, FROM, WHERE, JOIN```  Construire des requêtes d'insertion et de mise à jour à l'aide de : ```UPDATE, INSERT, DELETE```|On peut utiliser ```DISTINCT, ORDER BY``` ou les fonctions d'agrégation sans utiliser ```GROUP BY et HAVING```|

!!! capytale "Voir TP sur Capytal"

##  Du modèle relationnel au SGBD 


Nous allons maintenant d'aborder la partie logicielle : les SGBD (Systèmes de Gestion de Bases de Données).

Les SGBD jouent le rôle d'interface entre l'être humain et la base de données.  
Par l'intermédiaire de **requêtes**, l'utilisateur va consulter ou modifier la base de données. Le SGBD est garant de l'intégrité de cette base, et prévient notamment que les modifications ne soient pas préjudiciables à la base de données.

Le langage utilisé pour communiquer avec le SGBD est le langage **SQL**, pour Structured  Query Langage (pour *langage de requêtes structurées*).

Les SGBD les plus utilisés sont basés sur le modèle relationnel. Parmi eux, citons Oracle, MySQL, Microsoft SQL Server, PostgreSQL, Microsoft Access, SQLite, MariaDB...

Mais de plus en plus de SGBD **non-relationnels** sont utilisés, spécialement adaptés à des données plus diverses et moins structurées. On les retrouve sous l'appelation **NoSQL**  (pour *Not only SQL*). Citons parmi eux MongoDB, Cassandra (Facebook), BigTable (Google)...

La quasi-totalité de ces SGBD fonctionnent avec un modèle client-serveur. 

Nous allons travailler principalement avec le langage SQLite peut lui s'utiliser directement sans démarrer un serveur : la base de données est entièrement représentée dans le logiciel utilisant SQLite.   

## Création de tables

```sql
DROP TABLE IF EXISTS LIVRES;  
CREATE TABLE LIVRES
(code INT, titre TEXT, auteur TEXT, ann_publi INT, note INT, PRIMARY KEY (code));

```

### Création de la tables LIVRES

```sql
INSERT INTO LIVRES
(code,titre,auteur,ann_publi,note)
VALUES
(1,'1984','Orwell',1949,10),
(2,'Dune','Herbert',1965,8),
(3,'Fondation','Asimov',1951,9),
(4,'Le meilleur des mondes','Huxley',1931,7),
(5,'Fahrenheit 451','Bradbury',1953,7),
(6,'Ubik','K.Dick',1969,9),
(7,'Chroniques martiennes','Bradbury',1950,8),
(8,'La nuit des temps','Barjavel',1968,7),
(9,'Blade Runner','K.Dick',1968,8),
(10,'Les Robots','Asimov',1950,9),
(11,'La Planète des singes','Boulle',1963,8),
(12,'Ravage','Barjavel',1943,8),
(13,'Le Maître du Haut Château','K.Dick',1962,8),
(14,'Le monde des Ā','Van Vogt',1945,7),
(15,'La Fin de l’éternité','Asimov',1955,8),
(16,'De la Terre à la Lune','Verne',1865,10);
```

### Création de la table AUTEURS


```sql
DROP TABLE IF EXISTS AUTEURS;  
CREATE TABLE AUTEURS
(id INT, nom TEXT, prenom TEXT, ann_naissance INT, langue_ecriture TEXT, PRIMARY KEY (id)
);
```


```sql
INSERT INTO AUTEURS
(id,nom,prenom,ann_naissance,langue_ecriture)
VALUES
(1,'Orwell','George',1903,'anglais'),
(2,'Herbert','Frank',1920,'anglais'),
(3,'Asimov','Isaac',1920,'anglais'),
(4,'Huxley','Aldous',1894,'anglais'),
(5,'Bradbury','Ray',1920,'anglais'),
(6,'K.Dick','Philip',1928,'anglais'),
(7,'Barjavel','René',1911,'français'),
(8,'Boulle','Pierre',1912,'français'),
(9,'Van Vogt','Alfred Elton',1912,'anglais'),
(10,'Verne','Jules',1828,'français');
```

##  Sélection de données

### &#x2712;  Requête basique : SELECT, FROM


```sql
SELECT * 
FROM LIVRES
```




<table class="dataframe" border="1"><thead><tr style="text-align: right;"><th>code</th><th>titre</th><th>id_auteur</th><th>ann_publi</th><th>note</th></tr></thead><tbody><tr><td>1</td><td>1984</td><td>1</td><td>1949</td><td>10</td></tr><tr><td>2</td><td>Dune</td><td>2</td><td>1965</td><td>8</td></tr><tr><td>3</td><td>Fondation</td><td>3</td><td>1951</td><td>9</td></tr><tr><td>4</td><td>Le meilleur des mondes</td><td>4</td><td>1931</td><td>7</td></tr><tr><td>5</td><td>Fahrenheit 451</td><td>5</td><td>1953</td><td>7</td></tr><tr><td>6</td><td>Ubik</td><td>6</td><td>1969</td><td>9</td></tr><tr><td>7</td><td>Chroniques martiennes</td><td>5</td><td>1950</td><td>8</td></tr><tr><td>8</td><td>La nuit des temps</td><td>7</td><td>1968</td><td>7</td></tr><tr><td>9</td><td>Blade Runner</td><td>6</td><td>1968</td><td>8</td></tr><tr><td>10</td><td>Les Robots</td><td>3</td><td>1950</td><td>9</td></tr><tr><td>11</td><td>La Planète des singes</td><td>8</td><td>1963</td><td>8</td></tr><tr><td>12</td><td>Ravage</td><td>7</td><td>1943</td><td>8</td></tr><tr><td>13</td><td>Le Maître du Haut Château</td><td>6</td><td>1962</td><td>8</td></tr><tr><td>14</td><td>Le monde des Ā</td><td>9</td><td>1945</td><td>7</td></tr><tr><td>15</td><td>La Fin de l’éternité</td><td>3</td><td>1955</td><td>8</td></tr><tr><td>16</td><td>De la Terre à la Lune</td><td>10</td><td>1865</td><td>10</td></tr></tbody></table>




```sql
SELECT titre, auteur, note
FROM LIVRES
```




<table class="dataframe" border="1"><thead><tr style="text-align: right;"><th>titre</th><th>auteur</th><th>note</th></tr></thead><tbody><tr><td>1984</td><td>Orwell</td><td>10</td></tr><tr><td>Dune</td><td>Herbert</td><td>8</td></tr><tr><td>Fondation</td><td>Asimov</td><td>9</td></tr><tr><td>Le meilleur des mondes</td><td>Huxley</td><td>7</td></tr><tr><td>Fahrenheit 451</td><td>Bradbury</td><td>7</td></tr><tr><td>Ubik</td><td>K.Dick</td><td>9</td></tr><tr><td>Chroniques martiennes</td><td>Bradbury</td><td>8</td></tr><tr><td>La nuit des temps</td><td>Barjavel</td><td>7</td></tr><tr><td>Blade Runner</td><td>K.Dick</td><td>8</td></tr><tr><td>Les Robots</td><td>Asimov</td><td>9</td></tr><tr><td>La Planète des singes</td><td>Boulle</td><td>8</td></tr><tr><td>Ravage</td><td>Barjavel</td><td>8</td></tr><tr><td>Le Maître du Haut Château</td><td>K.Dick</td><td>8</td></tr><tr><td>Le monde des Ā</td><td>Van Vogt</td><td>7</td></tr><tr><td>La Fin de l’éternité</td><td>Asimov</td><td>8</td></tr><tr><td>De la Terre à la Lune</td><td>Verne</td><td>10</td></tr></tbody></table>



### &#x2712;  Requête basique : SELECT, FROM, WHERE


```sql
SELECT titre, ann_publi
FROM LIVRES
WHERE auteur='Asimov'
```

<table class="dataframe" border="1"><thead><tr style="text-align: right;"><th>titre</th><th>ann_publi</th></tr></thead><tbody><tr><td>Fondation</td><td>1951</td></tr><tr><td>Les Robots</td><td>1950</td></tr><tr><td>La Fin de l’éternité</td><td>1955</td></tr></tbody></table>


```sql
SELECT *
FROM LIVRES
WHERE auteur='Asimov'
```




<table class="dataframe" border="1"><thead><tr style="text-align: right;"><th>code</th><th>titre</th><th>auteur</th><th>ann_publi</th><th>note</th></tr></thead><tbody><tr><td>3</td><td>Fondation</td><td>Asimov</td><td>1951</td><td>9</td></tr><tr><td>10</td><td>Les Robots</td><td>Asimov</td><td>1950</td><td>9</td></tr><tr><td>15</td><td>La Fin de l’éternité</td><td>Asimov</td><td>1955</td><td>8</td></tr></tbody></table>




```sql
SELECT auteur,titre, ann_publi
FROM LIVRES
WHERE auteur='Asimov' AND note>=9
```




<table class="dataframe" border="1"><thead><tr style="text-align: right;"><th>auteur</th><th>titre</th><th>ann_publi</th></tr></thead><tbody><tr><td>Asimov</td><td>Fondation</td><td>1951</td></tr><tr><td>Asimov</td><td>Les Robots</td><td>1950</td></tr></tbody></table>

## &#x2712;  Renommage : AS
Pour rendre l'affichage plus "lisible" on peut renommer les colonnes : **AS**

- **Commande :**  
```sql
SELECT titre,auteur,ann_publi AS publication 
FROM LIVRES 
WHERE ann_publi >= 1945;
``` 
- **Traduction :**  
Lors de l'affichage du résulats et dans la suite de la requête (important), la colonne "ann_publi" est renommée "publication".


```sql
SELECT titre,auteur,ann_publi AS publication 
FROM livres 
WHERE ann_publi >= 1945;
```


<table class="dataframe" border="1"><thead><tr style="text-align: right;"><th>titre</th><th>auteur</th><th>publication</th></tr></thead><tbody><tr><td>1984</td><td>Orwell</td><td>1949</td></tr><tr><td>Dune</td><td>Herbert</td><td>1965</td></tr><tr><td>Fondation</td><td>Asimov</td><td>1951</td></tr><tr><td>Fahrenheit 451</td><td>Bradbury</td><td>1953</td></tr><tr><td>Ubik</td><td>K.Dick</td><td>1969</td></tr><tr><td>Chroniques martiennes</td><td>Bradbury</td><td>1950</td></tr><tr><td>La nuit des temps</td><td>Barjavel</td><td>1968</td></tr><tr><td>Blade Runner</td><td>K.Dick</td><td>1968</td></tr><tr><td>Les Robots</td><td>Asimov</td><td>1950</td></tr><tr><td>La Planète des singes</td><td>Boulle</td><td>1963</td></tr><tr><td>Le Maître du Haut Château</td><td>K.Dick</td><td>1962</td></tr><tr><td>Le monde des Ā</td><td>Van Vogt</td><td>1945</td></tr><tr><td>La Fin de l’éternité</td><td>Asimov</td><td>1955</td></tr></tbody></table>



### &#x2712;  Mettre dans l’ordre les réponses la clause ORDER BY
Il est aussi possible de rajouter la clause SQL ORDER BY afin d’obtenir les résultats classés dans un ordre
précis.



```sql
SELECT titre
FROM LIVRES
WHERE auteur='K.Dick' ORDER BY ann_publi
```




<table class="dataframe" border="1"><thead><tr style="text-align: right;"><th>titre</th></tr></thead><tbody><tr><td>Le Maître du Haut Château</td></tr><tr><td>Blade Runner</td></tr><tr><td>Ubik</td></tr></tbody></table>


!!! voc "Remarques :"
    - **Comportement par défaut :** Si le paramètre ASC ou DESC est omis, le classement se fait par ordre **croissant** (donc ASC est le paramètre par défaut).

## &#x2712;  La clause DISTINCT
Il est possible d’éviter les doublons grâce à la clause DISTINCT


```sql
SELECT auteur
FROM LIVRES
```


<table class="dataframe" border="1"><thead><tr style="text-align: right;"><th>auteur</th></tr></thead><tbody><tr><td>Orwell</td></tr><tr><td>Herbert</td></tr><tr><td>Asimov</td></tr><tr><td>Huxley</td></tr><tr><td>Bradbury</td></tr><tr><td>K.Dick</td></tr><tr><td>Bradbury</td></tr><tr><td>Barjavel</td></tr><tr><td>K.Dick</td></tr><tr><td>Asimov</td></tr><tr><td>Boulle</td></tr><tr><td>Barjavel</td></tr><tr><td>K.Dick</td></tr><tr><td>Van Vogt</td></tr><tr><td>Asimov</td></tr><tr><td>Verne</td></tr></tbody></table>


```sql
SELECT DISTINCT auteur
FROM LIVRES
```




<table class="dataframe" border="1"><thead><tr style="text-align: right;"><th>auteur</th></tr></thead><tbody><tr><td>Orwell</td></tr><tr><td>Herbert</td></tr><tr><td>Asimov</td></tr><tr><td>Huxley</td></tr><tr><td>Bradbury</td></tr><tr><td>K.Dick</td></tr><tr><td>Barjavel</td></tr><tr><td>Boulle</td></tr><tr><td>Van Vogt</td></tr><tr><td>Verne</td></tr></tbody></table>



### &#x2712;  La clause LIKE

On veut les titres de la table «livre» dont le titre contient la chaîne de caractères "Astérix".   
Le symbole ```%``` est un joker qui peut symboliser n'importe quelle chaîne de caractères. 

```sql
SELECT titre 
FROM livres 
WHERE titre LIKE 'F%';
```
permet d'obtenir les titres de livres commençant par F

```sql
SELECT titre 
FROM livres 
WHERE titre LIKE '%s';
```
permet d'obtenir les titres de livres finissant par s


```sql
 SELECT titre 
 FROM livres 
 WHERE titre LIKE 'F%';
```




<table class="dataframe" border="1"><thead><tr style="text-align: right;"><th>titre</th></tr></thead><tbody><tr><td>Fondation</td></tr><tr><td>Fahrenheit 451</td></tr></tbody></table>




```sql
SELECT titre 
FROM livres 
WHERE titre LIKE '%s';
```




<table class="dataframe" border="1"><thead><tr style="text-align: right;"><th>titre</th></tr></thead><tbody><tr><td>Le meilleur des mondes</td></tr><tr><td>Chroniques martiennes</td></tr><tr><td>La nuit des temps</td></tr><tr><td>Les Robots</td></tr><tr><td>La Planète des singes</td></tr></tbody></table>

## Opérations sur les données : sélection avec agrégation
 
 Les requêtes effectuées jusqu'ici ont juste sélectionné des données grâce à différents filtres : aucune action à partir de ces données n'a été effectuée.   

Nous allons maintenant effectuer des opérations à partir des données sélectionnées.  

On appelle ces opérations des **opérations d'agrégation**.

## &#x2712;  La clause COUNT

On veut compter le nombre d'enregistrements de la tables livres publiés en 1968.


```sql
 SELECT COUNT(*) AS total 
 FROM livres
 WHERE ann_publi=1968;
```




<table class="dataframe" border="1"><thead><tr style="text-align: right;"><th>total</th></tr></thead><tbody><tr><td>2</td></tr></tbody></table>




## &#x2712;  La clause  : SUM  - Additionner

- **Commande :** 
```sql
SELECT SUM(ann_publi) AS somme 
FROM livres
WHERE auteur LIKE "F%";
``` 
- **Traduction :** 

On veut additionner les années des livres de la tables livres commençant par F.   
Le résultat sera le seul élément d'une colonne nommée «somme».
*Attention : dans notre cas précis, ce calcul n'a aucun sens...*


<table class="dataframe" border="1"><thead><tr style="text-align: right;"><th>somme</th></tr></thead><tbody><tr><td>3904</td></tr></tbody></table>



## &#x2712;  La clause  : AVG  - Moyenne"

On veut calculer la moyenne des notes des livres de la table livres de l'auteur "Bradbury". Le résultat sera le seul élément d'une colonne nommée «moyenne».

```sql
SELECT AVG(note) AS note moyenne 
FROM livres
WHERE auteur="Bradbury";
```





<table class="dataframe" border="1"><thead><tr style="text-align: right;"><th>moyenne</th></tr></thead><tbody><tr><td>7.5</td></tr></tbody></table>



### &#x2712;  La clause  : MIN, MAX - Trouver les extremums:

- **Commande :**  
```sql
SELECT MIN(note) AS minimum 
FROM livres;
``` 


<table class="dataframe" border="1"><thead><tr style="text-align: right;"><th>auteur</th><th>titre</th><th>minimum</th></tr></thead><tbody><tr><td>Huxley</td><td>Le meilleur des mondes</td><td>7</td></tr></tbody></table>



## Des recherches croisées sur les tables : les jointures

 
Nous avons 2 tables, grâce aux jointures nous allons pouvoir associer ces 2 tables dans une même requête.

Repartons sur la bases LIVRES légèrement modifiées.



```sql
DROP TABLE IF EXISTS LIVRES;  
CREATE TABLE LIVRES
(code INT, titre TEXT, id_auteur TEXT, ann_publi INT, note INT, PRIMARY KEY (code,id_auteur));
```


```sql
INSERT INTO LIVRES
(code,titre,id_auteur,ann_publi,note)
VALUES
(1,'1984',1,1949,10),
(2,'Dune',2,1965,8),
(3,'Fondation',3,1951,9),
(4,'Le meilleur des mondes',4,1931,7),
(5,'Fahrenheit 451',5,1953,7),
(6,'Ubik',6,1969,9),
(7,'Chroniques martiennes',5,1950,8),
(8,'La nuit des temps',7,1968,7),
(9,'Blade Runner',6,1968,8),
(10,'Les Robots',3,1950,9),
(11,'La Planète des singes',8,1963,8),
(12,'Ravage',7,1943,8),
(13,'Le Maître du Haut Château',6,1962,8),
(14,'Le monde des Ā',9,1945,7),
(15,'La Fin de l’éternité',3,1955,8),
(16,'De la Terre à la Lune',10,1865,10);
```

### &#x2712; Jointures simples
En général, les jointures consistent à associer des lignes de 2 tables. Elles permettent d’établir un lien
entre 2 tables.

- **Commande :**  
```sql
SELECT *
FROM LIVRES
INNER JOIN AUTEURS ON LIVRES.id_auteur = AUTEURS.id
```
- **Traduction :** 
Comme plusieurs tables sont appelées, nous préfixons chaque colonne avec le nom de la table. 



<table class="dataframe" border="1"><thead><tr style="text-align: right;"><th>code</th><th>titre</th><th>id_auteur</th><th>ann_publi</th><th>note</th><th>id</th><th>nom</th><th>prenom</th><th>ann_naissance</th><th>langue_ecriture</th></tr></thead><tbody><tr><td>1</td><td>1984</td><td>1</td><td>1949</td><td>10</td><td>1</td><td>Orwell</td><td>George</td><td>1903</td><td>anglais</td></tr><tr><td>2</td><td>Dune</td><td>2</td><td>1965</td><td>8</td><td>2</td><td>Herbert</td><td>Frank</td><td>1920</td><td>anglais</td></tr><tr><td>3</td><td>Fondation</td><td>3</td><td>1951</td><td>9</td><td>3</td><td>Asimov</td><td>Isaac</td><td>1920</td><td>anglais</td></tr><tr><td>4</td><td>Le meilleur des mondes</td><td>4</td><td>1931</td><td>7</td><td>4</td><td>Huxley</td><td>Aldous</td><td>1894</td><td>anglais</td></tr><tr><td>5</td><td>Fahrenheit 451</td><td>5</td><td>1953</td><td>7</td><td>5</td><td>Bradbury</td><td>Ray</td><td>1920</td><td>anglais</td></tr><tr><td>6</td><td>Ubik</td><td>6</td><td>1969</td><td>9</td><td>6</td><td>K.Dick</td><td>Philip</td><td>1928</td><td>anglais</td></tr><tr><td>7</td><td>Chroniques martiennes</td><td>5</td><td>1950</td><td>8</td><td>5</td><td>Bradbury</td><td>Ray</td><td>1920</td><td>anglais</td></tr><tr><td>8</td><td>La nuit des temps</td><td>7</td><td>1968</td><td>7</td><td>7</td><td>Barjavel</td><td>René</td><td>1911</td><td>français</td></tr><tr><td>9</td><td>Blade Runner</td><td>6</td><td>1968</td><td>8</td><td>6</td><td>K.Dick</td><td>Philip</td><td>1928</td><td>anglais</td></tr><tr><td>10</td><td>Les Robots</td><td>3</td><td>1950</td><td>9</td><td>3</td><td>Asimov</td><td>Isaac</td><td>1920</td><td>anglais</td></tr><tr><td>11</td><td>La Planète des singes</td><td>8</td><td>1963</td><td>8</td><td>8</td><td>Boulle</td><td>Pierre</td><td>1912</td><td>français</td></tr><tr><td>12</td><td>Ravage</td><td>7</td><td>1943</td><td>8</td><td>7</td><td>Barjavel</td><td>René</td><td>1911</td><td>français</td></tr><tr><td>13</td><td>Le Maître du Haut Château</td><td>6</td><td>1962</td><td>8</td><td>6</td><td>K.Dick</td><td>Philip</td><td>1928</td><td>anglais</td></tr><tr><td>14</td><td>Le monde des Ā</td><td>9</td><td>1945</td><td>7</td><td>9</td><td>Van Vogt</td><td>Alfred Elton</td><td>1912</td><td>anglais</td></tr><tr><td>15</td><td>La Fin de l’éternité</td><td>3</td><td>1955</td><td>8</td><td>3</td><td>Asimov</td><td>Isaac</td><td>1920</td><td>anglais</td></tr><tr><td>16</td><td>De la Terre à la Lune</td><td>10</td><td>1865</td><td>10</td><td>10</td><td>Verne</td><td>Jules</td><td>1828</td><td>français</td></tr></tbody></table>



Des informations (id et id_auteur) sont en double.  
On peut être plus précis.


```sql
SELECT AUTEURS.nom,LIVRES.titre,LIVRES.note,AUTEURS.ann_naissance AS Naissance, LIVRES.ann_publi AS Publication, AUTEURS.langue_ecriture AS Langue
FROM LIVRES
INNER JOIN AUTEURS ON LIVRES.id_auteur = AUTEURS.id
ORDER BY AUTEURS.nom
```




<table class="dataframe" border="1"><thead><tr style="text-align: right;"><th>nom</th><th>titre</th><th>note</th><th>Naissance</th><th>Publication</th><th>Langue</th></tr></thead><tbody><tr><td>Asimov</td><td>Fondation</td><td>9</td><td>1920</td><td>1951</td><td>anglais</td></tr><tr><td>Asimov</td><td>Les Robots</td><td>9</td><td>1920</td><td>1950</td><td>anglais</td></tr><tr><td>Asimov</td><td>La Fin de l’éternité</td><td>8</td><td>1920</td><td>1955</td><td>anglais</td></tr><tr><td>Barjavel</td><td>La nuit des temps</td><td>7</td><td>1911</td><td>1968</td><td>français</td></tr><tr><td>Barjavel</td><td>Ravage</td><td>8</td><td>1911</td><td>1943</td><td>français</td></tr><tr><td>Boulle</td><td>La Planète des singes</td><td>8</td><td>1912</td><td>1963</td><td>français</td></tr><tr><td>Bradbury</td><td>Fahrenheit 451</td><td>7</td><td>1920</td><td>1953</td><td>anglais</td></tr><tr><td>Bradbury</td><td>Chroniques martiennes</td><td>8</td><td>1920</td><td>1950</td><td>anglais</td></tr><tr><td>Herbert</td><td>Dune</td><td>8</td><td>1920</td><td>1965</td><td>anglais</td></tr><tr><td>Huxley</td><td>Le meilleur des mondes</td><td>7</td><td>1894</td><td>1931</td><td>anglais</td></tr><tr><td>K.Dick</td><td>Ubik</td><td>9</td><td>1928</td><td>1969</td><td>anglais</td></tr><tr><td>K.Dick</td><td>Blade Runner</td><td>8</td><td>1928</td><td>1968</td><td>anglais</td></tr><tr><td>K.Dick</td><td>Le Maître du Haut Château</td><td>8</td><td>1928</td><td>1962</td><td>anglais</td></tr><tr><td>Orwell</td><td>1984</td><td>10</td><td>1903</td><td>1949</td><td>anglais</td></tr><tr><td>Van Vogt</td><td>Le monde des Ā</td><td>7</td><td>1912</td><td>1945</td><td>anglais</td></tr><tr><td>Verne</td><td>De la Terre à la Lune</td><td>10</td><td>1828</td><td>1865</td><td>français</td></tr></tbody></table>



## Modifications d'une base
 
 
### &#x2712; INSERT
 
 Insérer les données suivantes dans la base Auteurs:
```sql
INSERT INTO LIVRES
(code,titre,id_auteur,ann_publi,note)
VALUES
(17,'Hypérion','Simmons',1989,8)
```



### &#x2712; UPDATE
 


```sql
UPDATE LIVRES
SET note=7
WHERE titre = 'Hypérion'
```

### &#x2712; DELETE



```sql
DELETE FROM LIVRES
WHERE titre='Hypérion'
```
