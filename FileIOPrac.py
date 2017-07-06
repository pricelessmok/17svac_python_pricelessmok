#1
"""
f = open("newfile.txt",'w')
for i in range(10):
    data = "%d\n" %i
    f.write(data)
f.close()
"""

#2
"""
f = open("newfile.txt",'r')
line = f.readline()
print(line)
f.close()
"""

#3
f = open("newfile.txt",'r')
"""
while True:
    line = f.readline()
    if not line:
        break
    print(line)
"""
data = f.read()
print(data)
f.close()