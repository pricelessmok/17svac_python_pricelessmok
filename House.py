class HousePark:
    lastname = "박"
    def __init__(self, name):
        self.fullname = self.lastname + name
    def travel(self, where):
        print("%s %s"%(self.fullname,where))
    def love(self, other):
        print("%s %s love" % (self.fullname, other.fullname))
    def fight(self, other):
        print("%s %s fight" % (self.fullname, other.fullname))
    def __add__(self, other):
        print("%s %s married" % (self.fullname, other.fullname))
    def __sub__(self, other):
        print("%s %s divorced" % (self.fullname, other.fullname))

class HouseKim(HousePark):
    lastname = "김"
    def travel(self, where, day):
        print("%s %s %d" % (self.fullname, where, day))

pey = HousePark("응용")
juliet = HouseKim("줄리엣")
pey.love(juliet)
pey + juliet
pey.fight(juliet)
pey-juliet