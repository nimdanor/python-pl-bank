title=Calcul Mystere III


text==
La variable a est initialise avec la valeur 2.

La question est quelle est la valeur de la variable p a la fin de la suite d'instructions suivante:

{{formula}}


==



before==

import random

random.seed(seed)

formula="    a = 2\n    p = a * a\n"
a=2
p=a*a
for x in range(0,random.randint(2,4)):
    r=random.randint(0,10)
    if r <3 :
        formula += "    p *= a \n"
        p += p * a
    elif r <7:
        formula += "    p = p * a \n"
        p = p * a
    else:
        formula += "    p = p * p \n"
        p = p * p



text += """
 Mais cette fois ci nous souhaitons une reponse sous forme d'une expression simple.

Rappel: x**y en python signifie x a la puissance y."""
res=p
==


form=@ /forms/simpletextform.html


evaluator==
ret = response['answer']
if "p" in ret or "a" in ret:
    grade= False,"Une expression sans utiliser ni a ni p svp."
else:
    try:
        cal=float(ret)
        grade = False," Essai encore, mais sous forme d'une expression simple et pas sous forme numerique."
    except:
        try:
            cal=eval(ret)
            if cal == res:
                grade = True," Bien jouer ! "+str(ret)+" = " +str(res)
            else:
                grade = False," Essai encore "
        except :
            grade= False, " Formule Incorrecte"

==






