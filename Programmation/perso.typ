/*

\definecolor[named]{UGLiPurple}{HTML}{9F648C}
\definecolor[named]{UGLiRed}{HTML}{cc2936}
\definecolor[named]{UGLiOrange}{HTML}{eb8258}
\definecolor[named]{UGLiYellow}{HTML}{CFB04A}
\definecolor[named]{UGLiGreen}{HTML}{8FB349}
\definecolor[named]{UGLiDarkGreen}{HTML}{248935}
\definecolor[named]{UGLiBlue}{HTML}{267487}
\definecolor[named]{UGLiDarkBlue}{HTML}{1F466D}
*/

#set par(justify: true)

#let purple=rgb("#9F648C")
#let darkblue=rgb("1F466D")
#let green=rgb("8FB349")
#let darkgreen=rgb("248935")
#let orange=rgb("eb8258")

#let genericFramedText = (f_title,f_subtitle,f_content,f_color)=>{
  v(1em)
    block(
    fill: f_color.lighten(85%),
    inset: 8pt,  
    [
      #move(dx:-.5em,dy: -1.5em)[
        #block(
        fill: f_color,
        inset: .5em,
        radius: 2pt,text(fill:white)[*#f_title : #f_subtitle *] 
      )
      ]    
      #v(-2em) #f_content #v(.5em)
  ])
}

#let consigne = ()=>{genericFramedText("Consigne","","Le soin et la rédaction seront pris en compte dans la notation. Faites des phrases claires et précises.",orange)}

#let defi = (a,b)=>{genericFramedText("Définition",a,b,darkgreen)}

#let histoire = (a,b)=>{genericFramedText("Histoire",a,b,darkblue)}

#let python = (a)=>{genericFramedText("Code Python","",a,purple)}

#let exo = (a,b)=>{genericFramedText("Exercice",a,b,purple)}

#let correction = (a)=>{genericFramedText("Correction","",a,green)}

#let probleme = (a,b)=>{genericFramedText("Problème : ",a,b,darkblue)}

#let conclusion = (a)=>{genericFramedText("Conclusion","",a,red)}
