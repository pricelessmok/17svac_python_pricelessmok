def threeFive():
    total = 0
    for i in range(0,100):
        if (i%3==0) and (i%5==0):
            total+=i
    print(total)

threeFive()