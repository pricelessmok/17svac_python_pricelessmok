"""
#1
f = open("newfile.txt",'a')
for i in range (11,20):
    data = "%d\n" % i
    f.write(data)
f.close()
"""
#2
with open("newfile.txt","w") as f:
    f.write("hello my name is lee")