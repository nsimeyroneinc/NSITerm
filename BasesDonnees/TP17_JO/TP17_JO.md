<table  style="background-color: #E32636; width:100%;color:white;">
    <thead>
        <tr>
            <th style="text-align:center;border:solid;border-width:1px;font-size:20pt;width:70%;">TP n°17 : Retour sur le langage SQL - Les JO Londres 2012</th>
            <th style="text-align:center;border:solid;border-width:1px;font-size:12pt;width:30%">Thème  : Bases de données</th>
        </tr>
          <tr>
            <th style="text-align:center;border:solid;border-width:1px;font-size:15pt;width:70%;"></th>
            <th style="text-align:center;border:solid;border-width:1px;font-size:12pt;width:30%">EXERCICES</th>
        </tr>
    </thead>
</table>


![london-2012.jpg](data/JO.jpg){:.center}

Nous allons travailler sur une base de données liée aux Jeux Olympiques de Londres qui ont eu lieu en 2012.

## Partie 1 : Étude du schéma relationnel
Avec un ****éditeur de texte tout simple**** (type Notepad, Notepad++)

- ouvrir le fichier [create_JO.sql](https://capytale2.ac-paris.fr/web/sites/default/files/2021-09-15-17-50-13//ttt_fleleu/create_jo.sql);
- regarder les lignes qui définissent les différentes tables de la BDD et *sur une feuille de papier* ou sur un  *document numérique*, donner sous forme écrite son schéma relationnel en soulignant clés primaires (en trait plein) et clés étrangère (en pointillés).
- Pour savoir ce qu'est une clé primaire ou étrangère, renseignez vous auprès du cours.

## Partie 2 : Requêtes SQL

Exécuter les bonnes requêtes SQL pour obtenir les données suivantes.


### Requêtes sans jointures

!!! example "Q1."
     Afficher le nom et prénom des sportifs.


```

```
!!! example "Q2."
    Afficher les codes des pays dont viennent les sportifs par ordre alphabétique en éliminant les doublons.


```

```

!!! example "Q3."
    Afficher la liste des sportifs français (utiliser `cio = ’France’`).


```

```

!!! example "Q4."
    Afficher la liste des 301 disciplines triées par l’identifiant du sport auxquelles elles se rapportent.



```

```

!!! example "Q5."
    Afficher les noms des 86 pays situés après la France et avant la Russie (Russia) par ordre alphabétique.

    Utiliser les opérateurs `<` et `>`. 

    Remarquer que l’opérateur `BETWEEN` ne produit pas le résultat attendu (88 pays).


```

```

!!! example "Q6."
    Afficher les 98 identifiants de discipline dont au moins une épreuve a eu lieu entre le 27 et le 31 juillet 2012 inclus.


```

```

!!! example "Q7." 
    Afficher les noms des 61 sportifs qui sont soit français (FRA) soit britanniques (GBR).


```

```

!!! example "Q8."
    Afficher les intitulés des 131 disciplines contenant la chaîne de caractères « WOMEN ».


```

```

!!! example "Q9."
    Donner les 3 pays (CIO, nom) dont on ne connaît pas le code ISO2 ou ISO3 (utiliser le critère `IS NULL`).


```

```

!!! example "Q10."
    Donner les noms et prénoms des 2 sportifs dont le sexe est mentionné dans la BDD.


```

```

!!! example "Q11."
    À l’aide de la fonction `COUNT`, donner le nombre de sports (pas la liste).


```

```

!!! example "Q12."
    Donner le nombre de discipline(s) du sport d’identifiant 1 (pas la liste).


```

```

!!! example "Q13." 
    Combien de noms de familles différents sont portés par les sportifs ?


```

```

!!! example "Q14."
    Donner le nombre de pays n’ont pas d’ISO2.


```

```

!!! example "Q15."
    Donner le nombre de médailles d’or attribués lors de ces JO.


```

```

!!! example "Q16." 
    Afficher en une table le premier et le dernier évènement sportif de ces JO.


```

```

### Requêtes avec jointures

!!! example "Q17."
    Afficher la listes des noms et prénoms des sportifs européens.


```

```

!!! example "Q18."
    Afficher la liste des disciplines dépendant de l’athlétisme.


```

```

!!! example "Q19."
    Afficher toutes jours pendant lesquels un évènement lié à l’athlétisme eu lieu.


```

```

!!! example "Q20."
    Afficher les noms, prénoms et médailles gagnées par des sportifs dont le sexe figure dans la BDD.


```

```

!!! example "Q21."
    Afficher la liste des Français médaillés d’or.


```

```

!!! example "Q22."
    Afficher les noms, prénoms, sports et disciplines des sportifs ayant obtenu une médaille d’or.


```

```
