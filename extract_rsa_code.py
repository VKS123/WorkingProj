f=open("rabin.txt","r")
s=f.readlines()
f.close()
f=open("rabinmiller.txt","w")
for i in s:
    f.write(i[4:])
f.close()
