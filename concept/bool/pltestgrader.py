#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  pltestgrader.py
#  
#  Copyright 2018 Dominique Revuz <dr@univ-mlv.fr>
#  

from pltest_doc import PlRunner

from plutils import *
import json

from  sandboxio import get_answers, get_context,output


dic = get_context()

pltest = dic['pltest']

student=get_answers()['answer']


a,b = PlRunner(pltest,student).runpltest()

output(a,b)

print(json.dumps(dico_response))
