import doctest
import traceback


import feedback2




class PlRunner(doctest.DocTestRunner):
    def __init__(self,studentcode,pltest,fb = None):
        self.right = 0
        self.fail = 0
        self.total = 0
        self.testnum = -1
        if not fb :
            self.fb=feedback2.FeedBack()
        else:
            self.fb=fb
        self.student= studentcode
        self.pltest= pltest
        super().__init__()

    def runpltest(self):
        dic = {}
        # ~ with open("student.py","r") as f:
        # ~ exec(f.read(),dic)
        dic['__student']=self.student
        try:
            exec(self.student, dic)
        except Exception as e:
            self.fb.addTestError("Compilation ",str(e))
            return False,self.fb.getOutput()
        test = doctest.DocTestParser().get_doctest(self.pltest, dic, 'votre travail', 'foo.py', 0)
        self.run(test)
        print(self.fb.getOutput())
        return self.fb.grade(),self.fb.render()


    def testtitle(self, line):
            if line.endswith("\n"):
                line = line[:-1]
            if "#" not in line:
                return line
            else:
                if line.endswith("#"): # Hidden
                    return None
                found = line.split("#", 1) # couper sur le premier #
                if found[1].startswith("#"): # Numéro du test
                    return " "
                else:
                    return found[1]

    def report_start(self, out, test, example):
        pass
    def report_success(self, out, test, example, doc):
        sortie = self.testtitle(example.source)
        if sortie:
            self.fb.addTestSuccess(sortie)
            self.right += 1
            self.total += 1

    def report_failure(self, out, test, example, doc):
        sortie = self.testtitle(example.source)
        if sortie:
            self.fb.addTestFailure(sortie)
            self.fail += 1
            self.total += 1

    def report_unexpected_exception(self, out, test, example, exc_info):
        sortie = self.testtitle(example.source)
        self.total += 1
        if not sortie :
            self.fb.addTestError("Erreur ", str(exc_info[1]))
        else :
            self.fb.addTestError(sortie+": Test en echec ! ", str(exc_info[1]))

    def summarize(self):
        self.fb.doTextOutput()

   def grade(self):
       if self.globalok :
           return 100
        return 100*(self.right/self.total)

if __name__ == "__main__":
    pltest = """>>> A == 2
    True
    >>> titi==12     #Test titi initialisé à 12
    True
    >>> tiXti==12 ##
    True
    >>> taXi==12 # Test belbelbe
    True
    >>> TUTUTUTUTU==12 #
    True
    >>> __student.count("if") < 3 # Pas plus de Trois if
    True
    >>> __student.count("truc") > 4 #
    True
    """
    studentcode = "ZA=2;A=2;X=T"

    runner = PlRunner(studentcode , pltest,fb=feedback2.FeedBack())
    a,b = runner.runpltest()
    print(b)


    runner = PlRunner("A=2;titi=12" , pltest,fb=feedback2.FeedBack())
    a,b = runner.runpltest()
    if a:
        print("Bravo",b)
    else:
        print(b)


    #
    # runner = PlRunner("A=2;titi=12;jacques=11" , ">>> Caco==2 #\nTrue\n>>> A==2\nTrue\n>>> titi==12\nTrue",fb=feedback2.FeedBack())
    # a,b = runner.runpltest()
    # if a:
    #     print("Bravo")
    #     print(b)
    # else:
    #     print(b)

