# Découverte de la cryptographie

la cryptographie est une des applications majeures de l'informatique. Le but de projet est de réaliser un programme permettant de chiffrer et de déchiffrer un texte à l'aide du code de César, l'une des plus anciens (et des plus simples) méthode de cryptage. Le code de César peut être cassé par analyse fréquentielle, on programmera donc aussi le décryptage  du code de César en utilisant cette technique. Une autre partie du projet est consacrée au chiffrement de Vigenère.

## Etape 1 : le code de César

Comprendre le code de César et la méthode pour le déchiffrer. On pourra faire ses propres recherches ou consulter la vidéo suivante (en anglais, mais les sous-titres français sont disponibles):
<div class="centre"><iframe width="560" height="315" src="https://www.youtube.com/embed/sMOZf4GN3oc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div> 

Sans l'aide d'un ordinateur, *"à la main"* :

* Chiffrer le mot "EXPERT" en décalant les lettres de 5 emplacements.
* Déchiffrer de mot "DOBBSLVO" en sachant que la clé  est 10.

Préparer une explication orale de la méthode de chiffrement ainsi que le la technique de déchiffrement, inclure des exemples. 


## Etape 2 : Chiffrer ou déchiffrer avec la clé

Réaliser un programme permettant à un utilisateur de chiffrer ou de déchiffrer un texte avec la clé de son choix. Pour simplifier, on suppose que le texte est constitué uniquement de *lettres majuscules non accentuées*, de ponctuations et d'espaces. On écrira une fonction `chiffre_texte` qui prend en argument une chaine de caractère `texte` et une clé `cle` (entier compris entre 1 et 25) et qui renvoie `texte` chiffré avec le code de César de clé `cle` (on laisse intacte les espaces et caractères de ponctuation, on ne déchiffre que les lettres majuscules). Par exemple :
```pycon
>>> chiffre_texte("NSI",14)
'BGW'
>>> chiffre_texte("SUPER",5)
'XZUJW'
>>> chiffre_texte("C'EST GENIAL",11)
"N'PDE RPYTLW"
```

!!! aide
    * Penser à utiliser les fonctions `ord` et `chr` de Python
    * On pourra commencer par écrire une fonction `chiffre_caractere` qui prend en argument un caractère `caractere` et une clé `cle` et renvoie `caractere` décalé de `cle` emplacements. 


## Etape 3 : Analyse fréquentielle

Faire un programme qui décode automatiquement un texte crypté par la méthode de César grâce à une analyse fréquentielle. Tester votre programme sur l'exemple suivant :
```
PFOJC JCIG OJSN FSIGGW O RSQCRSF QS ASGGOUS
Q SGH HFSG PWSB AOWG WZ FSGHS SBQCFS PSOIQCID O TOWFS
```

!!! aide
    On pourra commencer par écrire une fonction `plus_frequent` qui prend en argument un texte et renvoie la lettre qui apparaît le plus souvent dans ce texte. Par exemple :
    ```pycon
    >>> plus_frequent("UN EXEMPLE DE TEXTE")
    'E'
    ```

## Etape 4 : dictionnaire et force brute

Tester votre programme sur le déchiffrement automatique du texte suivant :

```
RU YXDBBJ DW YAXOXWM BXDYRA, B'JBBRC MJWB BXW URC, B'JYYDHJWC BDA BXW YXUXLQXW. RU YARC DW AXVJW, RU U'XDEARC, RU UDC; VJRB RU W'H BJRBRBBJRC ZD'DW RVKAXPURX LXWODB, RU KDCJRC À CXDC RWBCJWC BDA DW VXC MXWC RU RPWXAJRC UJ BRPWRORLJCRXW.
```

Ce texte est extrait du livre *la disparition* (G. Perec), faire des recherches sur ce livre et expliquer sa particularité. Expliquer alors pourquoi le programme de déchiffrement par analyse fréquentielle ne fonctionne pas. 

Une autre méthode de décryptage consiste à utiliser une **attaque par force brute** c'est à dire qu'on teste toutes les clés possibles et on vérifie que les mots obtenus après déchiffrement sont des mots du dictionnaire. Mettre en oeuvre en Python cet algorithme de décryptage et l'utiliser pour le texte donné en exemple ci-dessus.

!!! aide
    On pourra télécharge ci-dessous un dictionnaire des mots de la langue française : 
    {{ telecharger("Dictionnaire","../files/projets/cesar/dictionnaire.txt")}}


## Etape 5 : Codage de Vigenère

Faire des recherches sur le codage de Vigenère, expliquer son fonctionnement, détailler un exemple de codage avec cette méthode. Ce code résiste-t-il à une approche par analyse fréquentielle ? Justifier. 

Proposer un programme Python permettant de coder et de décoder un texte avec la méthode de chiffrement de Vigenère.



**Bilbliographie :**  

- Ce cours s'inspire largement de celui de Fabrice Nativel.