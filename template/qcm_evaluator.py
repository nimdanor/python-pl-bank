#!/usr/bin/env python3
# coding: utf-8
import sys, jsonpickle
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

    if 'pairs' not in dic:
        print(" La balise 'pairs' obligatoire n'est pas définie dans votre exercice", file=sys.stderr)
        sys.exit(1)

    studentdic = get_answers()

    dic['pairs']

    if "feedback" in dic: # FIXME feedback devrai être un dictionnaire.
        outstr += dic["feedback"]

    output(a,outstr)


