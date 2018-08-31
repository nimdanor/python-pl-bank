

title=Racines

extends=/template/coding.pl




text==

Dans cet exercice nous cherchons a ecrire une fonction **racine** qui calcule une racine **{{typeracine}}**.

On definie en general la racine {{typeracine}} entiere de n comme l'entier $%r%$ telque
 l'inegalite suivante soit respecte:
    $%{{expnot}}%$.


==

pltest==
Ceci est la fonction racine.
==

before==
import random
import math
random.seed(seed)

l=[2,3,4,5,7]
ln=["Carre","Cubique","Quatrieme","Cinquieme","Septieme"]
p=random.randint(0,len(l)-1)
typeracine=ln[p]
exposant=l[p]
expnot="r^{"+str(exposant)+"}<=n<(r+1)^{"+str(exposant)+"}"
superieur="r^{"+str(exposant)+"}<n<=(r+1)^{"+str(exposant)+"}"
proche="abs(n-r^{"+str(exposant)+"})"

choix=random.choice(["proche","superieur",""])

if choix=="superieur" :
    text += """
Mais dans notre cas nous souhaitons connaitre la racine **superieur** l'entier $%r%$ telque
 l'inegalite suivante soit respecte:
    $%{{superieur}}%$."""
elif choix=="proche":
    text +="""Mais dans notre cas nous cherchons la racine la plus juste, c'est a dire l'entier telque sa puissance soit la plus proche de notre valeur $%n%$.
    Soit le $%r%$ telque $%{{proche}}%$ soit minimal.
    """

text += """
Ecrivez une fonction **racine** qui retourne la racine **{{typeracine}} {{choice}}** de son parametre.
"""

if choix == "superieur":
    f=lambda x: math.ceil(x**(1/exposant))
elif choix == "proche":
    f=lambda x:  round(x**(1/exposant))
else:
   f=lambda x:  math.floor(x**(1/exposant))

letest=""
for n in [1,999,1000,77777]:
    letest+= ">>> racine({})\n{}\n".format(n,f(n))

pltest += letest

text+="\n{{pltest}}"

==
