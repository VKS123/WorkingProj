import os
def enc(filenm):
    directory = filenm.split(".")[0]
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open("test1.pdf", "rb") as imageFile:
        f = imageFile.read()
        b = bytearray(f)
    res=""
    for i in b:
       res=res+chr(i)
    # f=open("message.txt","w")
    f=open(directory+"/"+"message.txt","w")
    f.write(res)
    f.close()
    return directory

def dec(filenm,extension):
    # f=open(directory+"/"+"final_decr.txt","r")
    f=open(filenm,"r")
    res=f.read()
    f.close()
    k=[]
    for i in res:
        k=k+[ord(i)]
    x=bytearray(k)
    fh = open("test."+extension, "wb")
    fh.write(x)
    fh.close()
