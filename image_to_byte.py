with open("IMG1.jpg", "rb") as imageFile:
  f = imageFile.read()
  b = bytearray(f)
print type(b)
print type(b[0])
res=""
for i in b:
    print i
    res=res+chr(i)
print len(b)
print res
print len(res)
k=[]
for i in res:
    k=k+[ord(i)]
x=bytearray(k)
print type(x)
print type(x[0])
for i in x:
    print i
    
fh = open("imageIMG11.jpg", "wb")
fh.write(x)
fh.close()
