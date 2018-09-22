#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#   feedback2.py
#  
#  Copyright 2018 Dominique Revuz <dr@univ-mlv.fr>
#



import jinja2

ERROR="error"
FAILURE="failure"
SUCCESS="success"


__doc__="""

La classe feedback permet de gerer l'evolution de l'évaluation d'un exercice.

Organisation de l'évaluation d'un exercice de programmation:

Deux parties:
 une partie erreurs:
    -> erreur de compilation 
    -> erreur de réponse (référence manquante pour répondre à la question)
    -> erreur de regle [ une règle de l'énoncé à été détournée ]
 une partie Tests :
    -> les tests ont 
        -> un numéro 
        -> un affichage [ soit un texte, soit une ligne de code] 
        -> un etat [success, failure, error ]


Comment utiliser feedback2 

    pour chaque test 
"""

# class CompositeFeedback():


class FeedBack():
    def __init__(self,name="",filename="template.html"):
        self.tests = []
        self.globalok = True  # if not true at least one problem
        self.numtest = 0
        self.name = str(name)
        self.filename=filename

    def addTestSuccess(self, text, got, want):
        self.numtest += 1
        self.tests.append((SUCCESS, self.numtest, text, got, want))

    def addTestFailure(self, text, got, want):
        self.numtest += 1
        self.globalok = False
        self.tests.append((FAILURE, self.numtest, text, got, want))

    def addTestError(self, text, error,para):
        self.globalok = False
        self.numtest += 1
        self.tests.append((ERROR, self.numtest, text, error, para))
        #self.addError("test", error)


    def _doTextOutput(self):
            print(getOutout())

    def getOutput(self):
        s=""
        for e,n,t,x,y in self.tests:
            s += "Test num :"+str(n)+" "+e+" "+t+" " +x+" "+ y +"\n"
        return s

    def __str__(self):
        return self.render()

    def render(self):
        with open(self.filename,"r") as tempfile:
            templatestring = tempfile.read()
        template = jinja2.Template(templatestring)
        x= template.render(feedback=self)
        return  x 




