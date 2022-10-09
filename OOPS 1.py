class python:
    def students(self):
        print("neel")
    def __init__(self):      #special function 
        print("raj")
c1=python()
c2=python()
c1.students()
#with parameter:
class python:
    def students(self,deg,proff):
        self.deg=deg
        self.proff= proff#the name should not be same
        print("stud_details=",self.deg,self.proff)

c1=python()    #C1=SELF
c1.students('BE','IT')
c2=python()
c2.students('BCA','JD')
class python:
    
    def __init__(self,deg,prof):
        self.deg= deg
        self.prof= prof
    def student(self):
        print(self.deg,self.prof)
        

c1=python("BE","IT")
c1.student()
class python:
    
    instution="besent" #class or static variables #global
    def __init__(self):
        self.deg= "BE" #instance variables 
        self.prof= "IT"
c1=python()
c2=python()
print(c1.deg,c1.instution)



class python:
    
    instution="besent" #class or static variables
    def __init__(self):
        self.deg= "BE" #instance variables 
        self.prof= "IT"
c1=python()
print(c1.deg,c1.instution)
c2=python()
c2.prof="audit" #changing the instance values
print(c2.prof)
python.instution="BS"# changing the class values
print(c1.deg,c1.instution)
'''methos are classified into 3 catogries

    instance method
    class method
    static method'''

class python1:
    instution ="besant"
    def __init__(self,w1,w2,w3):
        self.w1=w1
        self.w2=w2
        a=5
    @property    #
    def total(self):
        return (self.w1+self.w2+self.w3)
    @classmethod
    
    def inf(cls): # for class method
        return (cls.instution)
    @staticmethod          # nodefault parameter
    def com():
        print("the usual function")
    
    
c1= python1(5,4,4)
print(c1.total)
print(python1.inf())
python1.com()




