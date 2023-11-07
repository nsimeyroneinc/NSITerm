{% set num = 18 %}
{% set titre = "Récursivité" %}
{% set theme = "BAC" %}
{% set niveau = "terminale" %}


{{ titre_chapitre(num,titre,theme,niveau)}}

{{ initexo(0) }}


## Cours 

{{ aff_cours(num) }}






## Gestions de musiciens

!!! exo "D'après 2023, sujet zéro A"

*On pourra utiliser les mots clés SQL suivants :*

`AND`, `SELECT`, `FROM`, `WHERE`, `JOIN`, `INSERT INTO`, `VALUES`, `COUNT`, `ORDER BY`, `OR`, `ON`, `SET`, `UPDATE`.


On étudie une base de données permettant la gestion de l'organisation d'un festival de musique de jazz, dont voici le schéma relationnel comportant trois relations :


- la relation {{ relation("groupes", "id_groupe", "nom", "style", "nb_pers") }}
- la relation {{ relation("musiciens", "id_musicien", "nom", "prenom", "instru","#id_groupe") }}
- la relation {{ relation("concerts", "id_concert", "scene", "heure_debut", "heure_fin","#id_groupe") }}

Dans ce schéma relationnel :

- les clés primaires sont soulignées ;
- les clés étrangères sont précédées d'un #.
Ainsi `concerts.id_groupe` est une clé étrangère faisant référence à `groupes.id_groupe`.

Voici un extrait des tables **`groupes`**, **`musiciens`** et **`concerts`** :

!!! note "Extrait de **`groupes`**"
            
    | `id_groupe` |         `nom`          |     `style`     | `nb_pers` |
    | :---------: | :--------------------: | :-------------: | :-------: |
    |    `12`     |   `'Weather Report'`   | `'Jazz Fusion'` |    `5`    |
    |    `25`     |    `'The 3 Sounds'`    |  `'Soul Jazz'`  |    `4`    |
    |    `87`     | `'Return to Forever'`  | `'Jazz Fusion'` |    `8`    |
    |    `96`     | `'The Jazz Messenger'` |  `'Hard Bop'`   |    `3`    |

!!! note "Extrait de **`musiciens`**"

    | `id_musicien` |    `nom`    |  `prenom`   |      `instru`      | `id_groupe` |
    | :-----------: | :---------: | :---------: | :----------------: | :---------: |
    |     `12`      | `'Garrett'` |  `'Kenny'`  | `'saxophone alto'` |    `96`     |
    |     `13`      | `'Garrett'` |  `'Kenny'`  |     `'flute'`      |    `25`     |
    |     `58`      |  `'Corea'`  |  `'Chick'`  |     `'piano'`      |    `87`     |
    |     `97`      | `'Clarke'`  | `'Stanley'` |     `'basse'`      |    `87`     |


!!! note "Extrait de **`concerts`**"

    | `id_concert` | `scene` | `heure_debut` | `heure_fin` | `id_groupe` |
    | :----------: | :-----: | :-----------: | :---------: | :---------: |
    |     `10`     |   `1`   |  `'20 h 00'`  | `'20 h 45'` |    `12`     |
    |     `24`     |   `2`   |  `'20 h 00'`  | `'20 h 45'` |    `35`     |
    |     `36`     |   `1`   |  `'21 h 00'`  | `'22 h 00'` |    `96`     |
    |     `45`     |   `3`   |  `'18 h 00'`  | `'18 h 30'` |    `87`     |


**1.**  Citer les attributs de la table **`groupes`**.

??? success "Réponse"
    Les attributs de la table groupes sont : `id_groupe`, `nom`, `style` et `nb_pers`.

**2.**  Justifier que l'attribut `nom` de la table **`musiciens`** ne peut pas être une clé primaire.

??? success "Réponse"
    Une clé primaire doit être unique. Le nom `'Garrett'` apparait plusieurs fois, donc le nom ne peut être une clé primaire.
    
    On notera que le couple `(nom, prenom)` n'est pas non plus une clé primaire de cette table pour la même raison.
    
    De la même façon, le triplet `(nom, prenom, intru)` ne peut pas non plus être utilisé comme clé primaire : le même musicien peut tout à fait jouer du même instrument dans deux groupes différents.

**3.** En s'appuyant uniquement sur l'extrait des tables fourni ci-dessus écrire ce que renvoie la requête :

```sql
SELECT nom
FROM groupes
WHERE style = 'Jazz Fusion';
```

??? success "Réponse"
    La requête renvoie : `'Weather Report'` et `'Return to Forever'`.

**4.** Le concert dont l'`id_concert` est `36` finira à 22 h 30 au lieu de 22 h 00. 

Recopier sur la copie et compléter la requête SQL ci-dessous permettant de mettre à jour la relation **`concerts`** pour modifier l'horaire de fin de ce concert.

```sql
UPDATE concerts
SET ...
WHERE ... ;
```

??? success "Réponse"

    ```sql
    UPDATE concerts
    SET heure_fin = '22 h 30'
    WHERE id_concert = 36;
    ```

**5.** Donner une seule requête SQL permettant de récupérer le nom de tous les groupes qui jouent sur la scène 1.

??? success "Réponse"

    ```sql
    SELECT groupes.nom FROM groupes
    JOIN concerts ON concerts.id_groupe = groupes.id_groupe
    WHERE concerts.scene = 1;
    ```

**6.** Fournir une seule requête SQL permettant d'ajouter dans la relation **`groupes`** le groupe `'Smooth Jazz Fourplay'`, de style `'Free Jazz'`, composé de 4 membres. Ce groupe aura un `id_groupe` de 15. 

??? success "Réponse"
    ```sql
    INSERT INTO groupes (id_groupe, nom, style, nb_pers)
    VALUES (15, 'Smooth Jazz Fourplay', 'Free Jazz', 4);
    ```

Les données sont ensuite récupérées pour être analysées par la société qui produit les festivals de musique. Pour ce faire, elle utilise la programmation en Python afin d'effectuer certaines opérations plus complexes.

Elle stocke les données relatives aux musiciens sous forme d'un tableau de dictionnaires dans laquelle a été ajouté le nombre de concerts effectués par chaque musicien :

```python
>>> print(musiciens)
  [{'id_musicien': 12, 'nom': 'Garrett', 'prenom': 'Kenny',
    'instru': 'saxophone alto', 'id_groupe' : 96, 'nb_concerts': 5},
   {'id_musicien': 13, 'nom': 'Garrett', 'prenom': 'Kenny',
    'instru': 'flute', 'id_groupe' : 25, 'nb_concerts': 9},
   {'id_musicien': 58, 'nom': 'Corea', 'prenom': 'Chick',
    'instru': 'piano', 'id_groupe' : 87, 'nb_concerts': 4},
   {'id_musicien': 97, 'nom': 'Clarke', 'prenom': 'Stanley',
    'instru': 'basse', 'id_groupe' : 87, 'nb_concerts': 4},
   ...
  ]
```

**7.**  Écrire la fonction `recherche_nom` ayant pour unique paramètre un tableau de dictionnaires (comme `musiciens` présenté précédemment) renvoyant une liste contenant le nom de tous les musiciens ayant participé à au moins 4 concerts.

??? success "Réponse"

    ```python
    def recherche_nom(musiciens):
        resultat = []
        for musicien in musiciens:
            if musicien['nb_concerts'] >= 4:
                resultat.append(musicien['nom'])
        return resultat
    ```


## Centres Etrangers J1

!!! exo "D'après 2022, Centres étrangers, J1,Ex. 4"

!!! info "Rappel sur le langage SQL"
    Types de données

    | Type         | Description                                                                            |
    | ------------ | -------------------------------------------------------------------------------------- |
    | `CHAR(t)`    | Texte fixe de `t` caractères                                                           |
    | `VARCHAR(t)` | Texte de t caractères variables                                                        |
    | `TEXT`       | Texte de $65\,535$ caractères maximum                                                  |
    | `INT`        | Nombre entier de $-2^{31}$ à $2^{31} - 1$ (signé) ou de $0$ à $2^{32} - 1$ (non signé) |
    | `FLOAT`      | Réel à virgule flottante (approximation)                                               |
    | `DATE`       | Date format `AAAA-MM-JJ`                                                               |

    Quelques exemples de syntaxe SQL :
    
    - Insérer des enregistrements :
        - `#!sql INSERT INTO Table1 (attribut1, attribut2) VALUES (valeur1 , valeur2);`
    - Modifier des enregistrements :
        - `#!sql UPDATE Table1 SET attribut1=valeur1, attribut2=valeur2 WHERE Selecteur;`
    - Supprimer des enregistrements :
        - `#!sql DELETE FROM Table1 WHERE Selecteur;`
    - Sélectionner des enregistrements :
        - `#!sql SELECT attributs FROM Table1 WHERE Selecteur;`
    - Sélectionner des enregistrements dans un ordre ascendant :
        - `#!sql SELECT attributs FROM Table1 WHERE Selecteur ORDER BY attribut ASC;`
    - Sélectionner des enregistrements sans doublon :
        - `#!sql SELECT DISTINCT attributs FROM Table1 WHERE Selecteur;`
    - Effectuer une jointure :
        - `#!sql SELECT attributs FROM Table1 JOIN Table2 ON Table1.cle1=Table2.cle2 WHERE Selecteur;`



Dans le cadre d'une étude sur le réchauffement climatique, un centre météorologique rassemble des données. On considère que la base de données contient deux relations (tables). La relation **`Centres`** qui contient l'identifiant des centres météorologiques, la ville, la latitude, la longitude et l'altitude du centre. La relation **`Mesures`** qui contient l'identifiant de la mesure, l'identifiant du centre, la date de la mesure, la température, la pression et la pluviométrie mesurées.

Le schéma relationnel de la relation **`Centres`** est le suivant :

`#!sql Centres(id_centre: INT, nom_ville: VARCHAR, latitude: FLOAT, longitude: FLOAT, altitude: INT)`

Le schéma relationnel de la relation **`Mesures`** est le suivant :

`#!sql Mesures(id_mesure: INT, id_centre: INT, date_mesure: DATE, temperature: FLOAT, pression: INT, pluviometrie: INT)`

On fournit ci-dessous le contenu des deux relations.

!!! abstract "Relation **`Centres`**"

    | `id_centre` | `nom_ville`         | `latitude` | `longitude` | `altitude` |
    | ----------: | :------------------ | ---------: | ----------: | ---------: |
    |       `213` | `'Amiens'`          |   `49.894` |     `2.293` |       `60` |
    |       `138` | `'Grenoble'`        |   `45.185` |     `5.723` |      `550` |
    |       `263` | `'Brest'`           |   `48.388` |     `-4.49` |       `52` |
    |       `185` | `'Tignes'`          |   `45.469` |     `6.909` |     `2594` |
    |       `459` | `'Nice'`            |   `43.706` |     `7.262` |      `260` |
    |       `126` | `'Le Puy-en-Velay'` |   `45.042` |     `3.888` |      `744` |
    |       `317` | `'Gérardmer'`       |   `48.073` |     `6.879` |      `855` |


!!! abstract "Relation **`Mesures`**"

    | `id_mesure` | `id_centre` | `date_mesure` | `temperature` | `pression` | `pluviometrie` |
    | ----------: | ----------: | :------------ | ------------: | ---------: | -------------: |
    |      `1566` |       `138` | `'2021-10-29'` |        `8.0` |     `1015` |            `3` |
    |      `1568` |       `213` | `'2021-10-29'` |       `15.1` |     `1011` |            `0` |
    |      `2174` |       `126` | `'2021-10-30'` |       `18.2` |     `1023` |            `0` |
    |      `2200` |       `185` | `'2021-10-30'` |        `5.6` |      `989` |           `20` |
    |      `2232` |       `459` | `'2021-10-31'` |       `25.0` |     `1035` |            `0` |
    |      `2514` |       `213` | `'2021-10-31'` |       `17.4` |     `1020` |            `0` |
    |      `2563` |       `126` | `'2021-11-01'` |       `10.1` |     `1005` |           `15` |
    |      `2592` |       `459` | `'2021-11-01'` |       `23.3` |     `1028` |            `2` |
    |      `3425` |       `317` | `'2021-11-02'` |        `9.0` |     `1012` |           `13` |
    |      `3430` |       `138` | `'2021-11-02'` |        `7.5` |      `996` |           `16` |
    |      `3611` |       `263` | `'2021-11-03'` |       `13.9` |     `1005` |            `8` |
    |      `3625` |       `126` | `'2021-11-03'` |       `10.8` |     `1008` |            `8` |

**1.a.** Proposer une clé primaire pour la relation **`Mesures`**. Justifier votre choix.

??? success "Réponse"
    - `id_centre` n'est pas unique, elle ne peut pas servir de clé primaire.
    - `date_mesure` et `pluviometrie` non plus.
    - `temperature` et `pression` sont uniques, certes, pour l'instant, mais probablement pas ensuite, c'est un mauvais choix.

    `id_mesure` permet d'identifier de manière unique chaque mesure de la table ; c'est **la** bonne clé primaire pour cette relation.

**1.b.** Avec quel attribut peut-on faire une jointure entre la relation **`Centres`** et la relation **`Mesures`** ?

??? success "Réponse"
    La clé étrangère `id_centre` dans la table **`Mesures`** fait référence de manière unique à la clé primaire `id_centre` de la table **`Centres`**.

    Une jointure pourra être sans équivoque en utilisant l'égalité de ces deux champs.

**2.a.** Qu'affiche la requête suivante ?

```sql
SELECT * 
FROM Centres 
WHERE altitude > 500;
```

??? success "Réponse"
    La requête affiche tous les champs de la table **`Centres`** pour lesquels l'altitude est strictement supérieure à 500 m.


    | `id_centre` | `nom_ville`         | `latitude` | `longitude` | `altitude` |
    | ----------: | :------------------ | ---------: | ----------: | ---------: |
    |       `138` | `'Grenoble'`        |   `45.185` |     `5.723` |      `550` |
    |       `185` | `'Tignes'`          |   `45.469` |     `6.909` |     `2594` |
    |       `126` | `'Le Puy-en-Velay'` |   `45.042` |     `3.888` |      `744` |
    |       `317` | `'Gérardmer'`       |   `48.073` |     `6.879` |      `855` |


**2.b.** On souhaite récupérer le nom de la ville des centres météorologiques situés à une altitude comprise entre 700 m et 1200 m, inclus. Écrire la requête SQL correspondante.

??? success "Réponse"

    ```sql
    SELECT nom_ville 
    FROM Centres 
    WHERE altitude >= 700 AND altitude <= 1200;
    ```

    | `nom_ville`     |
    | :-------------- |
    | `'Le Puy-en-Velay'` |
    | `'Gérardmer'`       |

**2.c.** On souhaite récupérer la liste des longitudes et des noms des villes des centres météorologiques dont la longitude est supérieure à `5.0` La liste devra être triée par ordre alphabétique des noms de ville. Écrire la requête SQL correspondante.

??? success "Réponse"

    ```sql
    SELECT longitude, nom_ville
    FROM Centres
    WHERE longitude > 5.0
    ORDER BY nom_ville ASC;
    ```

    | `longitude` | `nom_ville` |
    | ----------: | :---------- |
    |     `6.879` | `'Gérardmer'`   |
    |     `5.723` | `'Grenoble'`    |
    |     `7.262` | `'Nice'`        |
    |     `6.909` | `'Tignes'`      |



**3.a.** Qu'affiche la requête suivante ?

```sql
SELECT * 
FROM Mesures 
WHERE date_mesure = '2021-10-30';
```

??? success "Réponse"
    La requête affiche tous les champs des enregistrements de la table **`Mesures`** pour la date du 30 octobre 2021.


    | `id_mesure` | `id_centre` | `date_mesure` | `temperature` | `pression` | `pluviometrie` |
    | ----------: | ----------: | :------------ | ------------: | ---------: | -------------: |
    |      `2174` |       `126` | `'2021-10-30'` |       `18.2` |     `1023` |            `0` |
    |      `2200` |       `185` | `'2021-10-30'` |        `5.6` |      `989` |           `20` |


**3.b.** Écrire une requête SQL permettant d'ajouter une mesure prise le 8 novembre 2021 dans le centre numéro 138, où la température était de 11°C, la pression de 1013 hPa et la pluviométrie de 0 mm. La donnée dont l'attribut est `id_mesure` aura pour valeur 3650.

??? success "Réponse"

    ```sql
    INSERT INTO Mesures (id_mesure, id_centre, date_mesure, temperature, pression, pluviometrie)
    VALUES (3650, 138, '2021-11-08', 11.0, 1013, 0);
    ```

**4.a.** Expliquer ce que renvoie la requête SQL suivante ?

```sql
SELECT * 
FROM Centres 
WHERE latitude = (SELECT MIN(latitude) FROM Centres);
```

??? success "Réponse"
    La requête imbriquée `#!sql SELECT MIN(latitude) FROM Centres;` renvoie `43.706` qui est la plus petite latitude parmi celle de la table **`Centres`**. Elle correspond à la latitude de Nice, la ville du centre le plus au Sud de cette table.

    Cette requête renvoie donc tous les champs du centre situé le plus au sud parmi ceux de la table **`Centres`**.


    | `id_centre` | `nom_ville` | `latitude` | `longitude` | `altitude` |
    | ----------: | :---------- | ---------: | ----------: | ---------: |
    |       `459` | `'Nice'`    |   `43.706` |     `7.262` |      `260` |



**4.b.** Écrire une requête SQL donnant la liste des villes dans lesquelles on a enregistré une température inférieure à 10°C en octobre 2021. On utilisera le mot clé `#!sql DISTINCT` afin d'éviter d'avoir des doublons. On rappelle que l'on peut utiliser les opérateurs de comparaison avec les dates.

??? success "Réponses"

    ```sql
    SELECT DISTINCT nom_ville
    FROM Centres
    JOIN Mesures
    ON Centres.id_centre = Mesures.id_centre
    WHERE Mesures.temperature < 10.0
    AND Mesures.date_mesure >= '2021-10-01'
    AND Mesures.date < '2021-11-01';
    ```

    | `nom_ville` |
    | :---------- |
    | `'Grenoble'`    |
    | `'Tignes'`      |
    | `'Gérardmer'`   |



## Évaluations d'élèves par compétence

!!! exo "D'après 2022, Centres étrangers, J2, Ex. 3"

!!! info "Rappel sur le langage SQL"
    Types de données

    | Type       | Description                                                                            |
    | ---------- | -------------------------------------------------------------------------------------- |
    | `CHAR`     | Chaine de caractères                                                                   |
    | `INT`      | Nombre entier de $-2^{31}$ à $2^{31} - 1$ (signé) ou de $0$ à $2^{32} - 1$ (non signé) |
    | `FLOAT`    | Réel à virgule flottante (approximation)                                               |
    | `DATE`     | Date format `AAAA-MM-JJ`                                                               |
    | `DATETIME` | Date et heure format `AAAA-MM-JJHH:MI:SS`                                              |

    Quelques exemples de syntaxe SQL :
    
    - Insérer des enregistrements :
        - `#!sql INSERT INTO Table1 (attribut1, attribut2) VALUES (valeur1 , valeur2);`
    - Modifier des enregistrements :
        - `#!sql UPDATE Table1 SET attribut1=valeur1, attribut2=valeur2 WHERE Selecteur;`
    - Supprimer des enregistrements :
        - `#!sql DELETE FROM Table1 WHERE Selecteur;`
    - Sélectionner des enregistrements :
        - `#!sql SELECT attributs FROM Table1 WHERE Selecteur;`
    - Effectuer une jointure :
        - `#!sql SELECT attributs FROM Table1 JOIN Table2 ON Table1.cle1=Table2.cle2 WHERE Selecteur;`


Les enseignants d'un établissement imaginaire proposent des parcours d'entrainement au numérique à leurs élèves en créant des séries d'exercices appelées **`Evaluations`**. Les différentes informations sont stockées dans une base de données.

Les informations de chaque campagne créée sont stockées dans la table **`Evaluations`** dont la structure est la suivante :

| Attribut           | Type   |
| ------------------ | ------ |
| `Code_evaluation`  | `CHAR` |
| `Nom_evaluation`   | `CHAR` |
| `Auteur`           | `CHAR` |
| `Date_evaluation`  | `CHAR` |
| `Code_competences` | `INT`  |


Un extrait de la table **`Evaluations`** est donné ci-dessous :

!!! abstract "_Tableau 1_"

    | `Code_evaluation` | `Nom_evaluation` | `Auteur`  | `Date_evaluation` | `Code_competences` |
    | ----------------- | ---------------- | --------- | ----------------- | ------------------ |
    | `'EXKVLX886'`     | `'Term7'`          | `'Peltier'` | `'13/10/2021'`      | `1453`         |
    | `'AZVBYB689'`     | `'Groupe3'`        | `'Lacour'`  | `'07/10/2021'`      | `1276`         |
    | `'PRJUYR491'`     | `'Term5'`          | `'Peltier'` | `'07/10/2021'`      | `1453`         |
    | `'RTKVLX656'`     | `'campagneSTMG'`   | `'Beley'`   | `'03/10/2021'`      | `476`          |
    | `'DZLYYR479'`     | `'Term5'`          | `'Serhani'` | `'27/09/2021'`      | `1659`         |
    | `'XJVBTX585'`     | `'grNSI2'`         | `'Eisen'`   | `'24/09/2021'`      | `532`          |
    | `'CRLYYR439'`     | `'1ere6'`          | `'Caille'`  | `'13/09/2021'`      | `532`          |
    | `'AZVBYB789'`     | `'rentreeHGGSP'`   | `'Martin'`  | `'13/09/2021'`      | `386`          |
    | `'OBJUYR491'`     | `'Web_2nde'`       | `'Boucher'` | `'07/09/2021'`      | `452`          |
    | `'AGTBYB689'`     | `'rechercheBTS'`   | `'Beley'`   | `'07/09/2021'`      | `1341`         |
    | `'DQVBTX905'`     | `'2nde2'`          | `'Nguyen'`  | `'07/09/2021'`      | `452`          |


**1.a.** Dans la table **`Evaluations`**, quel est le seul attribut pouvant servir de clé primaire ? Justifier votre réponse.

??? success "Réponse"
    
    Le seul attribut a avoir des valeurs unique est `Code_evaluation`, tous les autres peuvent créer des ambigüités lors de la désignation d'une entrée.
    
    La clé primaire doit donc être `Code_evaluation`.

**1.b.** Écrire la requête SQL d'insertion qui a permis d'enregistrer la campagne `Term7` dans la table **`Evaluations`**. Les informations relatives à cette campagne sont données dans la première ligne du tableau 1 précédent.

??? success "Réponse"
    
    ```sql
    INSERT INTO Evaluations 
    VALUES ('EXKVLX886', 'Term7', 'Peltier', '13/10/2021', 1453);
    ```

**2.** On suppose maintenant que la table **`Evaluations`** contient uniquement les 11 enregistrements présents dans le tableau 1.

**2.a.** Combien de lignes s'affichent après l'exécution de la requête suivante ?

```sql
SELECT auteur FROM Evaluations;
```

??? success "Réponse"
    
    Les résultats ne sont pas regroupés par auteur donc tous les auteurs sont renvoyés y compris les doublons : il y a 11 lignes.

**2.b.** Recopier les lignes issues de la requête suivante :

```sql
SELECT Nom_evaluation, Date_evaluation FROM Evaluations WHERE auteur = 'Peltier';
```

??? success "Réponse"
    
    | `Nom_evaluation` | `Date_evaluation` |
    | ---------------- | ----------------- |
    | `Term7`          | `13/10/2021`      |
    | `Term5`          | `07/10/2021`      |

**2.c.** Rédiger une requête permettant de connaitre le nom des campagnes prévoyant un entrainement ciblé sur le web (`Code_competences` $452$).

??? success "Réponse"
    
    ```sql
    SELECT Nom_evaluation
    FROM Evaluations
    WHERE Code_competences = 452;
    ```

**3.** Le système de gestion de bases de données dispose également d'une table **`Resultats`** dont la structure est la suivante :

| Attribut          | Type   |
| ----------------- | ------ |
| `Code_evaluation` | `CHAR` |
| `Num_eleve`       | `INT`  |
| `Score`           | `INT`  |

Si l'élève s'est connecté à la campagne, mais n'a pas cliqué sur « envoyer les résultats », son score vaut -1.

**3.a.** Qu'imposerait le choix du couple `(Code_evaluation, Num_eleve)` comme clé primaire pour la table **`Resultats`** ?

??? success "Réponse"
    
    On fait l'hypothèse que les `Num_eleve` sont tous uniques (un par élève).

    Une clé primaire ne doit être associée qu'à une entrée de la table. Choisir ce couple comme clé primaire imposerait que chaque élève ne fasse l'évaluation **qu'une seule fois**.

Un extrait de la relation est donné ci-dessous :

| `Code_evaluation` | `Num_eleve` | `Scores` |
| ----------------- | ----------- | -------- |
| `'PRJUYR491'`       | `17`        | `300`  |
| `'CRLYYR439'`       | `654`       | `-1`   |
| `'PRJUYR491'`       | `1454`      | `220`  |
| `'RTKVLX656'`       | `554`       | `255`  |
| `'DZLYYR479'`       | `17`        | `-1`   |
| `'XJVBTX585'`       | `1664`      | `12`   |
| `'CRLYYR439'`       | `18703`     | `0`    |
| `'PRJUYR491'`       | `1565`      | `422`  |
| `'XJVBTX585'`       | `12`        | `643`  |
| `'CRLYYR439'`       | `168`       | `19`   |
| `'DZLYYR479'`       | `17`        | `140`  |
| `'XJVBTX585'`       | `1658`      | `647`  |

**3.b.** Écrire une requête permettant d'obtenir les numéros des élèves (`Num_eleve`) qui ont travaillé la compétence `532`.

??? success "Réponse"
    
    ```sql
    SELECT Num_eleve
    FROM Resultats
    JOIN Evaluations ON Resultats.Code_evaluation = Evaluations.Code_evaluation
    WHERE Evaluation.Code_competences = 532
    ```


**4.a.** Proposer la structure d'une table **`Eleves`** permettant d'identifier les noms, prénoms et les classes des élèves.

??? success "Réponse"
    
    Là encore on fait l'hypothèse que chaque élève possède un `Num_eleve` unique.

    | Attribut    | Type   |
    | ----------- | ------ |
    | `Num_eleve` | `CHAR` |
    | `Nom`       | `CHAR` |
    | `Prenom`    | `CHAR` |
    | `Classe`    | `CHAR` |

**4.b.** Proposer une clé primaire pour cette table.

??? success "Réponse"
    
    La clé primaire serait `Num_eleve`.


## Données de visites de pages Web

!!! exo "D'après 2022, Polynésie, J1, Ex. 3"

!!! info "SQL"
    L'énoncé de cet exercice peut utiliser les mots du langage SQL suivants :

    `SELECT, FROM, WHERE, JOIN ON, INSERT INTO, VALUES, UPDATE, SET, DELETE, COUNT, DISTINCT, AND, OR, AS, ORDER BY, ASC, DESC`

Un site web recueille des données de navigation dans une base de données afin d'étudier les profils de ses visiteurs.  
Chaque requête d'interrogation d'une page de ce site est enregistrée dans une première table dénommée **`Visites`** sous la forme d'un 5-uplet : `(identifiant, adresse IP, date et heure de visite, nom de la page, navigateur)`.

Le chargement de la page `index.html` par `192.168.1.91` le 12 juillet 1998 à 22 h 48 aura par exemple été enregistré de la façon suivante :

`(1534, "192.168.1.91", "1998-07-12 22:48:00", "index.html", "Internet explorer 4.1")`.

Un extrait de cette table vous est donné ci-dessous :

|Identifiant | ip | dateheure | nompage | navigateur |
|:---|:---|:---|:---|:---|
| ... | ... | ... | ... | ... |
| 1534 | `"192.168.1.91"` | `"1998-07-12 22:48:00"`  | `"index.html"` | `"Internet explorer 4.1"` |
| 1535 | `"192.168.1.91"` | `"1998-07-12 22:49:05"`  | `"exercices.html"` | `"Internet explorer 4.1"` |
| 1536 | `"192.168.1.151"` | `"1998-07-12 22:59:44"`  | `"index.html"` | `"Netscape 6"` |
| 1537 | `"192.168.1.151"` | `"1998-07-12 23:00:00"`  | `"espace_enseignant.html"` | `"Netscape 6"` |
| 1538 | `"192.168.1.91"` | `"1998-07-12 23:29:00"`  | `"icorrection.html"` | `"Internet explorer 4.1"` |
| ... | ... | ...  | ... | ... |

**1.a)** Donner une commande d'interrogation en langage SQL permettant d'obtenir l'ensemble des 2-uplets `(adresse IP, nom de la page)` de cette table.

??? success "Réponse"

    ```sql
    SELECT ip, nompage 
    FROM Visites;
    ```


**1.b)** Donner une commande en langage SQL permettant d'obtenir l'ensemble des adresses IP ayant interrogé le site, sans doublon.

??? success "Réponse"

    ```sql
    SELECT DISTINCT ip 
    FROM Visites;
    ```


**1.c)** Donner une commande en langage SQL permettant d'obtenir la liste des noms des pages visitées par l'adresse IP `192.168.1.91`

??? success "Réponse"

    ```sql
    SELECT nompage 
    FROM Visites 
    WHERE ip = '192.168.1.91';
    ```

Ce site web met en place, sur chacune de ses pages, un programme en JavaScript qui envoie au serveur, à intervalle régulier de 15 secondes, le temps en secondes (`duree`) de présence sur la page. Ces envois contiennent tous la valeur de `identifiant` correspondant au chargement initial de la page.  
Par exemple, si le visiteur du 12 juillet 1998 est resté 65 secondes sur la page, celle-ci a envoyé au serveur les 4 doublets `(1534, 15)`, `(1534, 30)`, `(1534, 45)` et `(1534, 60)`.

Ces données sont enregistrées dans une table nommée **`Pings`**.

En plus de l'inscription d'une ligne dans la table **`Visites`**, chaque chargement d'une nouvelle page provoque l'insertion d'une ligne dans la table **`Pings`** comprenant l'identifiant de ce chargement et une durée de `0`.

Enfin, chaque ligne de la table **`Pings`** est unique, et ses deux colonnes contiennent toujours un `identifiant` et une `duree`.

L'attribut `identifiant` de la table **`Pings`** fait référence à l'attribut du même nom de la table **`Visites`** et les deux partagent les mêmes valeurs.

Un extrait de cette table vous est donné ci-dessous :

|Identifiant | duree |
|:---|:---|
| ... | ... |
| `1534` | `0` |
| `1534` | `15` |
| `1534` | `30` |
| `1534` | `45` |
| `1534` | `60` |
| ... | ... |
| `1536` | `0` |
| `1537` | `0` |
| `1537` | `15` |
| ... | ... |

**2.a)** De quelle table l'attribut `identifiant` est-il la clé primaire ?

??? success "Réponse"
    L'attribut `identifiant` est la clé primaire de la table **`Visites`**.

    Remarque : dans la table **`Pings`**, le doublet `(identifiant, duree)`  est clé primaire composite.

**2.b)** De quelle table l'attribut `identifiant` est-il une clé étrangère ?

??? success "Réponse"
    L'attribut `identifiant` est clé étrangère dans la table **`Pings`**.

**2.c)** On suppose que ces clés et règles (unicité, non nullité) ont été déclarées lors de la création des tables. Quelles vérifications sont automatiquement effectuées par le système de gestion de base de données ?

??? success "Réponse"
    Lors d'un enregistrement dans la table **`Pings`**, le système de gestion de base de données va vérifier :

    - la contrainte de domaine : le doublet inséré doit être un doublet du type spécifié dans la définition de la table, par exemple (entier, entier)
    - la contrainte d'unicité : on ne peut pas insérer deux fois le même doublet ;
    - les contraintes de non nullité : ni le champ `identifiant`, ni le champ `duree` ne peuvent être `NULL`
    - la contrainte d'intégrité référentielle : la valeur de l'attribut de la clé étrangère doit être inclus dans les valeurs de la clé primaire à laquelle il fait référence.

**3.** Le serveur reçoit le doublet `(identifiant, duree)` suivant : `(1534, 105)`. Écrire la commande SQL d'insertion qui permet d'ajouter cet enregistrement à la table **`Pings`**.

??? success "Réponse"

    ```sql
    INSERT INTO Pings VALUES (1534, 105);
    ```


On envisage ensuite d'optimiser la table en se contentant d'une seule ligne par identifiant dans la table **`Pings`** : les valeurs de l'attribut `duree` devraient alors être mises à jour à chaque réception d'un nouveau doublet `(identifiant, duree)`.

**4.a)** Écrire la requête de mise à jour permettant de fixer à 120 la valeur de l'attribut `duree` associée à l'identifiant 1534 dans la table **`Pings`**.

??? success "Réponse"

    ```sql
    UPDATE Pings 
    SET duree = 120 
    WHERE identifiant = 1534;
    ```

    Remarque : Dans le cadre de cette optimisation, l'attribut `identifiant` est clé primaire.

**4.b)** Expliquer pourquoi on ne peut pas être certain que les données envoyées par une page web, depuis le navigateur d'un client, via plusieurs requêtes formulées en JavaScript, arrivent au serveur dans l'ordre dans lequel elles ont été émises.

??? success "Réponse"
    Dans le protocole IP, les paquets sont routés indépendamment et peuvent donc éventuellement suivre des chemins différents s'il existe plusieurs itinéraires disponibles, ce qui peut impacter la durée d'acheminement. Une requête A envoyée avant une requête B peut donc arriver après cette dernière.

    Ainsi, on ne peut pas être certain que les données envoyées par une page web, depuis le navigateur d'un client, via plusieurs requêtes formulées en JavaScript, arrivent au serveur dans l'ordre dans lequel elles ont été émises.


**4.c)** En déduire qu'il est préférable d'utiliser une requête d'insertion plutôt qu'une requête de mise à jour pour ajouter des données à la table **`Pings`**.

??? success "Réponse"
    Il est préférable d'utiliser une requête d'insertion plutôt qu'une requête de mise à jour pour ajouter des données à la table **`Pings`** afin de s'assurer de conserver dans la table **`Pings`** un enregistrement représentatif du temps passé par un utilisateur sur une page donnée (dans ce cas, lors d'une requête sur la table **`Pings`**, il faudrait alors rechercher la valeur maximale relative à un identifiant de connexion donné).

    Remarque : il est en réalité techniquement possible d'empêcher de stocker une valeur qui diminuerait la durée, mais cela est hors programme.


**5.** Écrire une requête SQL utilisant le mot-clé `JOIN` et une clause `WHERE`, permettant de trouver les noms de toutes les pages qui ont été consultées plus d'une minute par au moins un utilisateur.

??? success "Réponse"

    ```sql
    SELECT DISTINCT Visites.nompage 
    FROM Visites 
    JOIN Pings ON Visites.identifiant = Pings.identifiant 
    WHERE Pings.duree > 60;
    ```
    Remarque 1 : le "par au moins un utilisateur" me fait utiliser le `DISTINCT` parce qu'il y aura des doublons si plusieurs utilisateurs ont consultée la même page assez longtemps, indépendamment de l'optimisation ou non.

    Remarque 2 : dans le cas où la clé est composite, il y aura en plus plusieurs fois la même page pour une même consultation si la durée est >= 75. Ce n'est pas important pour lister les pages, mais ça l'est si on veut les compter ensuite (y compris si on fait du `GROUP BY`).

    Remarque 3 : dans le cas où l'optimisation a été faite, ces doublons de même consultation n'existeront pas, mais le cas de multiples utilisateurs consultant la même page reste. La requête est inchangée.

