class HousePark:
    lastname = "박"
    def __init__(self, name):
        self.fullname = self.lastname + name
    def travel(self, where):
        print("%s,%s으로 떠나다" %(self.fullname, where))

temp = HousePark("응용")
temp.travel("부산")