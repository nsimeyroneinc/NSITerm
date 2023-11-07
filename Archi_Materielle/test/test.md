---
maxWidth: 600
---

# myMarkmap

## Un outil libre <BR>  et gratuit

### [Sources](https://github.com/eyssette/myMarkmap/) sur Github
### _Auteur_ : [Cédric Eyssette](https://eyssette.github.io/)
### Créé à partir du <BR>  logiciel [markmap](https://markmap.js.org/)

## Pour faire des <BR>  cartes mentales

- Clic sur ✒️ en haut à gauche <br> (_raccourci clavier : `e`_) pour <br>**éditer** sa carte mentale.  On <BR> utilise  la syntaxe **Markdown** <BR> pour créer des branches
  - `# Titre`  <BR> pour le niveau 1
  - `## Sous-titre` <BR>  pour le niveau 2
  - `### Niveau 3`, <BR>  `#### Niveau 4` <BR> … ensuite
  - Ou bien, on fait une liste à puces <BR> `- Niveau 3` <BR> 　`  - Niveau 4` <BR> `- Niveau 3` <BR> (on ajoute 2 espaces avant  <BR> pour  passer à un autre niveau)
- Clic sur 👓   pour **cacher** la <BR>  fenêtre d'édition et **voir**  <BR> seulement la carte mentale <BR> (_raccourci clavier : `Escape`_)
- Clic sur 💾 pour **enregistrer**  <BR> la carte au format _svg_ [image fixe] <BR> (_raccourci clavier : `s`_) <BR> Clic sur 🌐 pour **enregistrer** au <BR>format HTML [interactivité possible] <BR>(_raccourci clavier : `h`_) 
- Clic sur 🔗 pour copier un **lien** <BR>  de **partage** de la carte mentale <BR> dans le presse-papier <BR> (_raccourci clavier : `l`_)
- Clic sur les **cercles** à l'intersection <BR> des différentes branches pour <BR> **afficher ou masquer la suite**

## Usages plus <BR>  avancés <!--fold-->

### Des balises pour <BR> **contrôler l'affichage** <BR> de la carte

#### **Markdown** 

- `**texte**` : pour mettre en **gras**
- `_texte_` : pour mettre en _italiques_
- `[lien](URL)` : pour insérer un [lien](https://eyssette.github.io/)
- `![](URL)` : pour insérer une image
	- `![h-25](URL)` : pour spécifier la hauteur  <BR>de l'image (de h-25, h-50 … à h-200)
- ``` `code` ``` : Pour insérer du `code` 
- `==texte==`: Pour surligner du ==texte==
- `++texte++`: Pour souligner du ++texte++

#### **HTML**

- `<br>` ou `<BR>` pour forcer le passage à la ligne
- `<span style="...">texte</span>` <BR> pour changer le style d'un élément
  
#### **Autres <BR> balises**

- `<!--fold-->` en fin de ligne pour que les <BR> sous-branches soient cachées par défaut : <BR> il faut cliquer sur le cercle pour afficher la suite<!-- fold-->
    - Cette branche est cachée par défaut !
    - Cette branche aussi !
- `:code_emoji:` : pour insérer un code pour un emoji [:link:](https://raw.githubusercontent.com/omnidan/node-emoji/master/lib/emoji.json)
- `{{partie masquée}}` pour masquer une partie <BR> d'un texte :  voici par exemple un {{passage}} masqué <BR> (cliquer dessus pour afficher / masquer à nouveau)

#### **En-tête** <BR> (YAML)

- Pour spécifier la largeur <BR> maximale d'une branche
- Pour ajouter des styles <BR>CSS spécifiques
- Pour ajouter un titre
- Exemple :
  -  `---` <BR> `maxWidth: 300` <BR> `style: strong{color:red}` <BR> `title: Titre de la carte` <BR> `---`


### Possibilité d'utiliser un <BR> **fichier externe**

- On peut mettre son texte <BR> **sur une forge** et l'afficher <BR> avec myMarkmap
	- <BR> `https://mymarkmap.vercel.app/#URL`
	- En cas de problème : <BR> `https://mymarkmap.vercel.app/#https://api.allorigins.win/raw?url=URL`