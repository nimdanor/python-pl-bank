#!/usr/bin/env python3
# coding: utf-8
import sys, json, jsonpickle, time
from sandboxio import output, get_context, get_answers

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

    from pltest_doc import PlRunner
    dic = get_context()
    if "pltest" not in dic and "pltest0" not in dic:
        print("No pltest neither pltest0-n  defined change template", file=sys.stderr)
        sys.exit(1)
    pltest = dic['pltest']
    import feedback2
    student = get_answers()['answer']
    outstr=""
    tester = PlRunner(student,pltest)
    a, b = tester.runpltest(0)
    i=0
    while "pltest"+str(i) in dic and a==100:
        #outstr += "<h3> Test suite "+str(i)+"</h3>"+b
        outstr += b
        testi = PlRunner(student,dic["pltest"+str(i)])
        a, b = testi.runpltest(i+1)
        i=i+1

    outstr +=  b

    output(a,outstr)


