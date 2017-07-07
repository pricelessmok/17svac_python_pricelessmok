class HousePark:
    lastname = "박"
    def __init__(self, name):
        self.fullname = self.lastname + name
    def travel(self, where):
        print("%s,%s으로 떠나다" %(self.fullname, where))

temp = HousePark("응용")
temp.travel("부산")

class HouseKim(HousePark):
    lastname = "김"
    def travel(self, where, day):
        print("%s, %s여행 %d일 감" % (self.fullname,where,day))

temp2 = HouseKim("수지")
temp2.travel("춘천",5)