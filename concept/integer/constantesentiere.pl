

# TODO accents

# oneshot=True

tag=constants|integer|base


title= Constantes entiere

before=@ intvalues.py
evaluator=@ intvalues.py

evaluator+=
b,t = check(response['answer'], V,B)
t= t+" "+ str(V)+"  "+str(B)
grade= b,t

==


text==

Python permet d'ecrire des constantes entieres dans quatres bases differentes 2,8,10,16.

Soit les bases: Binaire, Octale, Decimale (usuelle), et Hexadecimale.

Pour preciser la base dans laquelle est ecrit la constante une indication doit ^etre donnee :

Les constantes decimales ne commencent pas par Zero.

Les autres commencent par:

1. 0b ou 0B pour les constantes Binaires.
2. 0o ou 0O pour les constantes Octales.
3. 0x ou 0X pour les constantes heXadecimales.

==


before+=
import random
import time
random.seed(seed)

B=random.choice([2,8,16])
V=random.randint(2,17)
text += "Ecrivez la valeur {} en base {} ({})".format(V,B,basename(B))

==



form==
<div class="input-group">
    <input id="form_txt_answer"  class="form-control" placeholder="" style="weigth:150" required>
</div>
==


