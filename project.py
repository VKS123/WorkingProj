import base64
##f=open("message.txt","w")
##with open("test.pdf", "rb") as imageFile:
##    st = base64.b64encode(imageFile.read())
##    print len(st)
##    x=len(str(st))
##    print x
##    print x/127
##    print x%127
##    f.write(str(st))
##f.close()

f=open("final_decr.txt","r")
s=f.read()
f.close()
st= bytes(s)
fh = open("test1.pdf", "wb")
fh.write(st.decode('base64'))
fh.close()
