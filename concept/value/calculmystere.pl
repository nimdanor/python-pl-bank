title=Calcul Mystere

template=/template/simpleeval.pl


basetext==
La variable a est initialise avec la valeur 2.

La question est quelle est la valeur de la variable p a la fin de la suite d'instructions suivante:

==

tag=operator_**|expression

before==

import random

random.seed(seed)

formula="    a = 2\n    p = a * a\n"
a=2
p=a*a
for x in range(0,random.randint(1,3)):
    r=random.randint(0,10)
    if r <7 :
        formula += "    p = p * a \n"
        p = p * a
    else:
        formula += "    p = p * p \n"
        p = p * p


text = basetext+ formula

res=p
==


# form=@ lib:/forms/simplenumeric.html
form==

<!-- Form numerique -->

<div class="input-group">
    <input id="form_answer" type="number" class="form-control" placeholder="" required>
</div>

==

evaluator==
if not response['answer']:
    grade= False," Repondez quelque chose !"
elif int(response['answer']) == res:
    grade = True," Bien joué ! "+str(res)
else:
    grade = False," Réessayez "
==




