<table  style="background-color: #E32636; width:100%;color:white;">
    <thead>
        <tr>
            <th style="text-align:center;border:solid;border-width:1px;font-size:20pt;width:70%;">TD n°18 : Retour sur le langage SQL - Sujet BAC</th>
            <th style="text-align:center;border:solid;border-width:1px;font-size:12pt;width:30%">Thème  : Bases de données</th>
        </tr>
          <tr>
            <th style="text-align:center;border:solid;border-width:1px;font-size:15pt;width:70%;">FRANCE Sujet 2 - Juin 2021</th>
            <th style="text-align:center;border:solid;border-width:1px;font-size:12pt;width:30%">SUJET BAC</th>
        </tr>
    </thead>
</table>


Une restauratrice a mis en place un site Web pour gérer ses réservations en ligne. Chaque client peut s’inscrire en saisissant ses identifiants. Une fois connecté, il peut effectuer une réservation en renseignant le jour et l’heure. Il peut également commander son menu en ligne et écrire un avis sur le restaurant.  
Le gestionnaire du site Web a créé une base de données associée au site nommée restaurant, contenant les quatre relations du schéma relationnel ci-dessous :  

![sql](data/BAC_SQL.png){:.center}

Dans le schéma relationnel précédent, un attribut souligné indique qu’il s’agit d’une clé primaire. Un attibut précédé du symbole # indique qu’il s’agit d’une clé étrangère et la flèche associée indique l’attribut référencé. Ainsi, par exemple, l'attribut idPlat de la relation Commande est une clé étrangère qui fait référence à l'attribut idPlat de la relation Plat.  
Dans la suite, les mots clés suivants du langage SQL pourront être utilisés dans les requêtes :

```sql
SELECT, FROM, WHERE, JOIN, ON, DELETE, UPDATE, SET, INSERT INTO, AND, OR.
```

!!! example "Question 1"
    Parmi les trois requêtes suivantes, écrites dans le langage SQL, laquelle renvoie les valeurs de tous les attributs des plats de la catégorie 'entrée' :  

    - R1 :  
    ```sql    
    SELECT nom, prix
    FROM Plat
    WHERE categorie = 'entrée';
    ```

    - R2 :  
    ```sql   
    SELECT *
    FROM Plat
    WHERE categorie = 'entrée';
    ```

    - R3 :  
    ```sql   
    R3 : UPDATE Plat
    SET categorie = 'entrée'
    WHERE 1;
    ```

!!! example "Question 2"
    Écrire, dans le langage SQL, des requêtes d’interrogation sur la base de données restaurant permettant de réaliser les tâches suivantes :  

    a. Afficher les noms et les avis des clients ayant effectué une réservation pour la date du '2021-06-05' à l’heure '19:30:00'.  
    b. Afficher le nom des plats des catégories 'plat principal' et 'dessert', correspondant aux commandes de la date '2021-04-12'.


!!! example "Question 3"
    Que réalise la requête SQL suivante ?  

    ```sql  
    INSERT INTO Plat
    VALUES(58,'Pêche Melba', 'dessert', 'Pêches et glace vanille', 6.5);
    ```

!!! example "Question 4"
    Écrire des requêtes SQL permettant de réaliser les tâches suivantes :  

    a. Supprimer les commandes ayant comme idReservation la valeur 2047.  
    b. Augmenter de 5% tous les prix de la relation plat strictement inférieurs à 20.00.  
    