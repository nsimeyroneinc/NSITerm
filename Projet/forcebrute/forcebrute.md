# Attaque par force brute


La première partie du projet consiste à déterminer des mots de passe en utilisant une [*attaque par force brute*](https://www.cnil.fr/fr/definition/force-brute-attaque-informatique){target=_blank}. Les mots de passe protègent des fichiers `pdf` et il faudra utiliser Python pour générer des mots de passe et les tester jusqu'à trouver le bon. Une seconde partie du projet est la création d'un programme Python permettant de générer automatiquement des mots de passe forts.

On utilise dans ce projet le module `pymupdf` de Python permettant d'interagir avec des fichiers au format `pdf`. Pour installer ce module, écrire en ligne de commande : 
```
pip install pymupdf
```

On donne ci-dessous une fonction Python `test_password` qui prend en argument une chaine de caractères `password` et renvoie `True` lorsque `password` est le mot de passe permettant d'ouvrir le fichier `FILE` déclaré en constante au début du programme :

```python linenums="1"
import fitz

FILE = "protege1.pdf"
DOC = fitz.Document(FILE)


def test_password(password):
    '''Renvoie True lorsque password permet d'ouvrir le fichier FILE déclaré ci-dessus'''
    return DOC.authenticate(password)
```

Par exemple pour tester si la mot de passe du fichier `protege1` est "1789", on peut par exemple faire :

```python
if test_password("1789"):
    print("Le mot de passe est 1789")
```
Attention, le fichier sur lequel on effectue le test est donné à la ligne 3 dans la variable `FILE`.

## Etape 1 : Avec des chiffres

Ces deux premiers fichiers ne devraient pas poser problème : les mots de passe ne contiennent que des chiffres !

### Fichier 1
* Fichier à télécharger :

{{ telecharger("Fichier1","../files/projets/forcebrute/protege1.pdf") }}

* Informations sur le mot de passe:  
Vous savez que ce mot de passe contient 4 caractères qui sont tous des chiffres. C'est à dire que ce mot de passe est semblable à un code de carte bancaire, comme par exemple `1492` ou `0141`.

### Fichier 2

* Fichier à télécharger :

{{ telecharger("Fichier2","../files/projets/forcebrute/protege2.pdf") }}


* Informations sur le mot de passe:  
Vous savez que ce mot de passe est une date de naissance au format `jjmmaaaa` et que l'année de naissance est supérieure à 1900. 

!!! aide
    Afin d'optimiser votre programme et de ne pas tester inutilement des mots de passe, attention à bien générer des dates de naissances valides ! 

## Etape 2 : avec des lettres aussi !

### Fichier 3

* Fichier à télécharger :

{{ telecharger("Fichier3","../files/projets/forcebrute/protege3.pdf") }}


* Informations sur le mot de passe:  
Vous savez que ce mot de passe est un mot de la langue française écrit en minuscule. Pour vous aider, un dictionnaire peut être téléchargé  ci-dessous :
{{ telecharger("Dictionnaire","../files/projets/cesar/dictionnaire.txt")}}


### Fichier 4
* Fichier à télécharger :

{{ telecharger("Fichier4","../files/projets/forcebrute/protege4.pdf") }}


* Informations sur le mot de passe:  
Les mots de passe les plus courants ont été répertoriés sur ce [site](https://github.com/tarraschk/richelieu){target=_blank}. Le quatrième mot de passe figure dans cette liste de mots de passe couramment utilisée.



## Etape 3 : à peine plus compliqué !

### Fichier 5 
* Fichier à télécharger :
{{ telecharger("Fichier5","../files/projets/forcebrute/protege5.pdf") }}

* Informations sur le mot de passe:
De nombreuses personnes utilisent leur prénom (écrit avec une majuscule) suivi de leur numéro de département comme mot de passe comme par exemple `Kevin974` pour un habitant de la Réunion se prénommant Kevin. C'est le cas pour ce mot de passe ou vous savez de plus que le prénom est courant (il figure dans le top100 des prénoms les plus attribués en France ces dernières années)

## Etape 4 : générateur de mots de passe

Ecrire un programme Python permettant de générer des mots de passe aléatoires résistants à une attaque par force brute. L'utilisateur pourra préciser les caractères à utiliser (chiffres, majuscules, minuscules, caractères spéciaux) et la longueur du mot de passe souhaité.

## Etape 5 : pour aller plus loin

Ecrire un programme Python permettant de déterminer le temps approximatif nécessaire pour trouver un mot de passe par une attaque par force brute en fonction de la longueur du mot de passe et du type de caractère utilisé.


**Bilbliographie :**  

- Ce cours s'inspire largement de celui de Fabrice Nativel.
