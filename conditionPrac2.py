coffee = 10
price = 300

while True:
    print("coffee %d" % coffee)
    money = int(input("넣어주세요\n"))
    if money == price:
        print("coffee")
        coffee -= 1
    elif money > price:
        print("change %d" %(money - price))
        coffee -= 1
    else:
        print("return money")
    if not coffee:
        print("no coffee")
        break