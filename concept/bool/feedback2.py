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
    def __init__(self):
        self.tests = []
        self.errors = []
        self.globalok = True  # if not true at least one problem
        self.numtest = 0

    def addTestSuccess(self, text):
        self.numtest += 1
        self.tests.append((SUCCESS, self.numtest, text))

    def addTestFailure(self, text):
        self.numtest += 1
        self.globalok = False
        self.tests.append((FAILURE, self.numtest, text))

    def addTestError(self, text, error):
        self.globalok = False
        self.numtest += 1
        self.tests.append((ERROR, self.numtest, text+error))
        #self.addError("test", error)

    # def __addError(self, typeerror, error):
    #     self.errors.append((typeerror, error))
    #     self.globalok = False

    # def compileError(self, error):
    #     self.addError("compile", error)
    #
    # def ruleError(self, error):
    #     self.addError("rule", error)

    def _doTextOutput(self):
        if not self.globalok :
            print("Problemes avec votre solution")
            for e,t in self.errors:
                print(e+":"+t)
        for e,n,t in self.tests:
            print("Test num :"+str(n)+" "+e+" "+t)

    def getOutput(self):
        s=""
        if not self.globalok :
            s+="Problemes avec votre solution\n"
            for e,t in self.errors:
                s += e+":"+t+"\n"
        for e,n,t in self.tests:
            s += "Test num :"+str(n)+" "+e+" "+t+"\n"
        return s

    def __str__(self):
        return getOutput()

    def render(self):
        with open("template.html","r") as tempfile:
            templatestring = tempfile.read()
        template = jinja2.Template(templatestring)
        x= template.render(feedback=self)
        return x
