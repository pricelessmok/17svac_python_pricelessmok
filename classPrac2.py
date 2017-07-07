#1
class FourCal:
    def setdata(self,a,b):
        self.a = a
        self.b = b
    def getsum(self):
        return self.a+self.b
    def getsub(self):
        return self.a-self.b

a = FourCal()
a.setdata(2,3)

print(a.a)
print(a.b)
print(a.getsum())
print(a.getsub())

#2
class HousePark:
    lastname = "박"
    def setname(self, name):
        self.fullname = self.lastname + name
    def travel(self, where):
        print("%s, %s를 가다\n" % (self.fullname, where))

pey = HousePark()
pes = HousePark()
pey.setname("응용")
pey.travel("부산")

print(pey.fullname)
print(pes.lastname)