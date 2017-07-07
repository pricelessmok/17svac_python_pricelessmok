#1
class Calc:
    def __init__(self):
        self.result=0
    def adder(self, num):
        self.result += num
        return self.result

calc1 = Calc()
calc2 = Calc()

print(calc1.adder(3))
print(calc1.adder(4))
print(calc2.adder(3))
print(calc2.adder(7))

#2
class Service:
    secret = "secret"
    def setname(self, name):
        self.name = name
    def sum(self,a,b):
        result = a+b
        print("%s %d" %(self.name,result))

svc = Service()
svc.setname("lee")
print(svc.secret)
print(svc.sum(3,6))

#__init__의 정의