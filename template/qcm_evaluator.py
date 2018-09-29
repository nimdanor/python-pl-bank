#!/usr/bin/env python3
# coding: utf-8
import sys, jsonpickle
from sandboxio import output, get_context, get_answers

def calculategrade(enonce, studentdic, dic):
    """
    :param enonce: [(" affirmation1",True),("affirmation2",False],(" affirmation3",True),("affirmation4",False],]
    :param studentdic: ["anwser_1":['on'], "anwser_2":['on']]
    :return:
    if unscrosfalse :
        2,4  (answer1 and answer4 correct over 4 possible points
    else:
        1,2 answer1 correct and answer3 not correct
    """
    uncrosedfalse = ( 'uncrosedfalse' in dic and dic['uncrosedfalse'] )

    total = 0
    for i,(x,b) in enumerate(enonce):
        q='answer_'+str(i)
        if b and  q in studentdic:
            total += 1
            a+= 1
        elif uncrosedfalse:
            total += 1
            if q not in studentdic:
                a += 1
     return a, total



missing_evaluator_stderr = """\
The key 'evaluator' was not found in the context.
When using this grader, the PL must declare a script inside a key 'evaluator'. This script have
access to every variable declared in the PL and its 'before' script.
It should declare a variable 'grade' which should contain a tuple (int, feedback) where int is the grade between [0, 100]."""
missing_grade_stderr = """\
'evaluator' did not declare the variable 'grade'. 
The script have access to every variable declared in the PL and its 'before' script.
It should declare a variable 'grade' which should contain a tuple (int, feedback) where int is the grade between [0, 100]."""
if __name__ == "__main__":
    if len(sys.argv) < 5:
        msg = ("Sandbox did not call grader properly:\n"
               + "Usage: python3 grader.py [input_json] [output_json] [answer_file] [feedback_file]")
        print(msg, file=sys.stderr)
        sys.exit(1)
    dic=get_context()
    if 'pairs' not in dic:
        print(" La balise 'pairs' obligatoire n'est pas définie dans votre exercice", file=sys.stderr)
        sys.exit(1)
    a=0
    total = len(dic['pairs'])
    studentdic = get_answers()
    a, t= calculategrade(dic(['pairs']),studentdic)
    dic['grade']= (100*a)/t
    if "feedback" in dic: 
        import jinja2
        if a==total:
            if 'success' in dic["feedback"]:
                outstr = jinja2.Template(dic["feedback"]['success']).render(dic)
            else:
                outstr = '<div class="btn-success">  Bravo ! </div>'
        else:
            if 'failure' in dic["feedback"]:
                outstr = jinja2.Template(dic["feedback"]['failure']).render(dic)
            else:
                outstr = '<div class="btn-danger">  Raté ! '+ str(a)+"/"+str(total)+ '</div>'
    output(grade,outstr)


