def ep2023(annee):
        aff="\n"
        aff+= "|Numéro | Enoncé en ligne | Lien de téléchargement| Thème exercice 1 | Thème exercice 2  | Code fourni |Correction|\n"
        aff+= "|-------|---| -----------------------|------------------|-------------------|-------------|----------|\n"
        FNAME = f"officiels/Annales/EP/{annee}/l{annee}.txt"
        icones = {"N":":star:","B":"<span class='rouge'>:material-bug:</span>","D":"<span class='navy'>:material-bomb:</span>","M":":fontawesome-solid-square-root-variable:","W":"<span class='orange'>:fontawesome-solid-triangle-exclamation:</span>"}
        with open(FNAME,"r",encoding="utf-8") as f:
            nums=1
            for s in f:
                lf=s.split(",")
                if '0' in lf[3]:
                    correction = f"Voir 2022"
                else:
                    #dossier={annee}-S{str(nums).zfill(2)}
                    correction = f"[{annee}-S{str(nums).zfill(2)}](../../Corriges/{annee}-S{str(nums).zfill(2)}/)"
                    #enonce1 = f"[{annee}-S{str(nums).zfill(2)}](../../../officiels/Annales/EP/{annee}/{dossier}/)"
                    #enonce2 = f"[{annee}-S{str(nums).zfill(2)}](../../../officiels/Annales/EP/{annee}/{annee}-S{str(nums)_2)/{enonce}.zfill(2)}/)"
                dnums ="**" +str(nums)+"** "
                for letter in icones:
                    if letter in lf[5]:
                        dnums = dnums + icones[letter]
                aff+=f"|{dnums}| |[Sujet N°{nums}](../../../officiels/Annales/EP/{annee}/{lf[0]}/{lf[0]}.pdf) | {lf[2]} | {lf[3]} | [:material-download: Code](../../officiels/Annales/EP/{annee}/{lf[0]}/{lf[0]}.py) | {correction} |\n"
                nums+=1
        return aff
    

ep2023(2023)