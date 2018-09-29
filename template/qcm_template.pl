
title= template qcm

text= Cochez les affirmations correctes.


good==
La lune tourne
0 est plus petit que 1 
Mars est dite: la planète rouge 
le sucre est blanc
le cheval blanc de Henri VI est blanc
==

nb=8

bad==
La terre est plate 
Le soleil tourtne autour de la terre 
Les satélites de la lune sont rouges.
1 est plus petit que 0

==

barem=reponsescorrecte
# uniquement les vraies

form=""

feedback.success="<div class="btn-success"> Voila votre resultat : {{  grade }} </div>"

feedback.failure="<div class="btn-danger"> Voila votre resultat : {{  grade }} </div>"


builder=@ /builder/before.py
before=@ qcm_build.py
grader=@qcm_evaluator.py
@ /utils/sandboxio.py


