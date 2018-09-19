title=test de pltest_doc 

@ pltest_doc.py
@ /pysrc/src/plutils.py

code==
A=2
B=3
==

pltest==
>>> A == A # A existe 
True
>>> B == B # B Existe
True
>>> A==2 # A vaut 2 
True
>>> B==3 
True
==

@ evaluator.py [grader.py]
@ feedback2.py

@/pysrc/src/__init__.py

@/pysrc/src/plutils.py
@/pysrc/src/pldoctest.py
#@/pysrc/src/template.html
@ /utils/sandboxio.py




# une interface standard d'exercice avec un editeur pour la réponse
form=@ /python/form/editorform.html
