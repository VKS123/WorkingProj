##keysize,rsize
##mlen=(keysize-rsize)/8
##k0
##padding_file
##rfile
def msg_to_binary(msg):
    res=""
    for i in msg:
        v=bin(ord(i))[2:]
        res=res+('0'*(8-len(v)))+v
    return res
def binary_to_string(bi):
    res=""
    i=0
##    if len(bi)%8==0:
##        print "yes"
##    else:
##        print "no"
    while i<len(bi)/8 :
        split_msg=bi[8*i:8*(i+1)]
        res=res+chr(int(split_msg,2))
        i=i+1
    return res
    
f=open("rsa_privkey.txt","r")
val=f.read()
f.close()
res=val.split(",")
keysize=int(res[0])
n=int(res[1])

f=open("random_file.txt","r")
rval=f.read()
f.close()
res1=rval.split(",")
rsize=int(res1[0])
r=int(res1[1])
G=int(res1[2])

split=(keysize-rsize)/rsize

f=open("message.txt","r")
msg=f.read()
f.close()

mlen=len(msg)
pad_list=[]
if mlen%split==0:
    i=0
    while i<mlen/split:
        split_msg=msg[split*i:split*(i+1)]
        M=msg_to_binary(split_msg,rsize)
        X=(int(M,2))^G
        Xbin=bin(X)[2:]
        XX='0'*(split-len(Xbin))+Xbin
        H=XX[:rsize]
        Y=(int(H,2))^r
        Ybin=bin(Y)[2:]
        YY='0'*(rsize-len(Ybin))+Ybin
        pad_plain=int(XX+YY,2)
        f=open("msg"+str(i+1)+".txt","w")
        f.write(str(pad_plain))
        f.close()
        pad_list=pad_list+[0]
        i=i+1
    f=open("padding_bits.txt","w")
    for i in pad_list:
        f.write(str(i))
        f.write("\n")
    f.close()
else:
    k0=(split-(mlen%split))*rsize
    i=0
    while i<mlen/split:
        split_msg=msg[split*i:split*(i+1)]
        M=msg_to_binary(split_msg)
        X=(int(M,2))^G
        Xbin=bin(X)[2:]
        XX='0'*(split-len(Xbin))+Xbin
        H=XX[:rsize]
        Y=(int(H,2))^r
        Ybin=bin(Y)[2:]
        YY='0'*(rsize-len(Ybin))+Ybin
        pad_plain=int(XX+YY,2)
        f=open("msg"+str(i+1)+".txt","w")
        f.write(str(pad_plain))
        f.close()
        pad_list=pad_list+[0]
        i=i+1
    split_msg=msg[split*(mlen/split):]
    M=msg_to_binary(split_msg)
    M=M+'0'*k0
    X=(int(M,2))^G
    Xbin=bin(X)[2:]
    XX='0'*(split-len(Xbin))+Xbin
    H=XX[:rsize]
    Y=(int(H,2))^r
    Ybin=bin(Y)[2:]
    YY='0'*(rsize-len(Ybin))+Ybin
    pad_plain=int(XX+YY,2)
    f=open("msgpad.txt","w")
    f.write(str(pad_plain))
    f.close()
    pad_list=pad_list+[k0]
    f=open("padding_bits.txt","w")
    for i in pad_list:
        f.write(str(i))
        f.write("\n")
    f.close()


f=open("padding_bits.txt","r")
pad_0_list=map(int,f.readlines())
f.close()
for i in range(len(pad_0_list)):
    if i==len(pad_0_list)-1:
        if pad_0_list[-1]==0:
            filename="msg"+str(i+1)+".txt"
        else:
            filename="msgpad.txt"
    else:
        filename="msg"+str(i+1)+".txt"
    f=open(filename,"r")
    s=f.read()
    f.close()
    k0=pad_0_list[i]
    pad=int(s)
    Y=bin(pad)[-rsize:]
    X=bin(pad)[2:-rsize]
    H=X[:rsize]
    rr=int(Y,2)^int(H,2)
    x=bin(rr)[2:]
    res=(x*(split/rsize))+x[:(split%rsize)]
    G=int(res,2)
    M=int(X,2)^G
    if k0==0:
        MM=bin(M)[2:]
        MM='0'*((split*rsize)-len(MM))+MM
    else:
        MM=bin(M)[2:-k0]
        MM='0'*((split*rsize)-k0-len(MM))+MM
    MMM=binary_to_string(MM)
    print MMM
    filenm="decr"+str(i+1)+".txt"
    f=open(filenm,"w")
    f.write(MMM)
    f.close()

final=""
for i in range(len(pad_0_list)):
    filenm="decr"+str(i+1)+".txt"
    f=open(filenm,"r")
    s=f.read()
    f.close()
    final=final+s
f=open("final_decr.txt","w")
f.write(final)
f.close()
