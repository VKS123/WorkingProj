import sys
import shutil
DEFAULT_BLOCK_SIZE = 256 # 128 bytes
BYTE_SIZE = 256 # One byte has 256 different values.

#def main(MODE):

def main(MODE,directory,prikeyfile,pubkeyfile):
    mode = MODE # set to 'encrypt' or 'decrypt'

    if mode == 'encrypt':
        # pubKeyFilename = 'rsa_pubkey.txt'
        pubKeyFilename = pubkeyfile
        # f=open("padding_bits.txt","r")
        f = open(directory + "/" + "padding_bits.txt", "r")
        pad_0_list=map(int,f.readlines())
        f.close()
        for i in range(len(pad_0_list)):
            if i==len(pad_0_list)-1:
                if pad_0_list[-1]==0:
                    # filenm="msg"+str(i+1)+".txt"
                    filenm=directory + "/" + "msg"+str(i+1)+".txt"
                    # filename="encrypted_file"+str(i+1)+".txt"
                    filename=directory + "/" + "encrypted_file"+str(i+1)+".txt"
                else:
                    # filenm="msgpad.txt"
                    filenm=directory + "/" + "msgpad.txt"
                    # filename="encrypted_file_pad.txt"
                    filename=directory + "/" + "encrypted_file_pad.txt"
            else:
                # filenm="msg"+str(i+1)+".txt"
                filenm=directory + "/" + "msg"+str(i+1)+".txt"
                # filename="encrypted_file"+str(i+1)+".txt"
                filename=directory + "/" + "encrypted_file"+str(i+1)+".txt"
            f=open(filenm,"r")
            s=f.read()
            f.close()
            message = s
            print('Encrypting and writing to %s...' % (filename))
            encryptedText = encryptAndWriteToFile(filename, pubKeyFilename, message)

            print('Encrypted text:')
            print(encryptedText)
        shutil.make_archive('Enc', 'zip', directory)

    elif mode == 'decrypt':
        # privKeyFilename = 'rsa_privkey.txt'
        privKeyFilename = prikeyfile
        # f=open("padding_bits.txt","r")
        f = open(directory + "/" + "padding_bits.txt", "r")
        pad_0_list=map(int,f.readlines())
        f.close()
        for i in range(len(pad_0_list)):
            if i==len(pad_0_list)-1:
                if pad_0_list[-1]==0:
                    filenm=directory + "/" + "msg"+str(i+1)+".txt"
                    filename=directory + "/" + "encrypted_file"+str(i+1)+".txt"
                else:
                    filenm=directory + "/" + "msgpad.txt"
                    filename=directory + "/" + "encrypted_file_pad.txt"
            else:
                filenm=directory + "/" + "msg"+str(i+1)+".txt"
                filename=directory + "/" + "encrypted_file"+str(i+1)+".txt"
            print('Reading from %s and decrypting...' % (filename))
            decryptedText = readFromFileAndDecrypt(filename, privKeyFilename)
            f=open(filenm,"w")
            f.write(decryptedText)
            f.close()
            print('Decrypted text:')
            print(decryptedText)


def getBlocksFromText(message, blockSize=DEFAULT_BLOCK_SIZE):

    messageBytes = message.encode('ascii') # convert the string to bytes

    blockInts = []
    for blockStart in range(0, len(messageBytes), blockSize):
        blockInt = 0
        for i in range(blockStart, min(blockStart + blockSize, len(messageBytes))):
            blockInt = blockInt+(ord(messageBytes[i]) * (BYTE_SIZE ** (i % blockSize)))
        blockInts.append(blockInt)
    return blockInts


def getTextFromBlocks(blockInts, messageLength, blockSize=DEFAULT_BLOCK_SIZE):
    message = []
    for blockInt in blockInts:
        blockMessage = []
        for i in range(blockSize - 1, -1, -1):
            if len(message) + i < messageLength:
                asciiNumber = blockInt // (BYTE_SIZE ** i)
                blockInt = blockInt % (BYTE_SIZE ** i)
                blockMessage.insert(0, chr(asciiNumber))
        message.extend(blockMessage)
    return ''.join(message)


def encryptMessage(message, key, blockSize=DEFAULT_BLOCK_SIZE):
    encryptedBlocks = []
    n, e = key

    for block in getBlocksFromText(message, blockSize):
        # ciphertext = plaintext ^ e mod n
        encryptedBlocks.append(pow(block, e, n))
    return encryptedBlocks


def decryptMessage(encryptedBlocks, messageLength, key, blockSize=DEFAULT_BLOCK_SIZE):
    decryptedBlocks = []
    n, d = key
    for block in encryptedBlocks:
        # plaintext = ciphertext ^ d mod n
        decryptedBlocks.append(pow(block, d, n))
    return getTextFromBlocks(decryptedBlocks, messageLength, blockSize)


def readKeyFile(keyFilename):
    fo = open(keyFilename)
    content = fo.read()
    fo.close()
    keySize, n, EorD = content.split(',')
    return (int(keySize), int(n), int(EorD))


def encryptAndWriteToFile(messageFilename, keyFilename, message, blockSize=DEFAULT_BLOCK_SIZE):
    keySize, n, e = readKeyFile(keyFilename)

    if keySize < blockSize * 8: # * 8 to convert bytes to bits
        sys.exit('ERROR: Block size is %s bits and key size is %s bits. The RSA cipher requires the block size to be equal to or less than the key size. Either decrease the block size or use different keys.' % (blockSize * 8, keySize))


    encryptedBlocks = encryptMessage(message, (n, e), blockSize)

    for i in range(len(encryptedBlocks)):
        encryptedBlocks[i] = str(encryptedBlocks[i])
    encryptedContent = ','.join(encryptedBlocks)

    encryptedContent = '%s_%s_%s' % (len(message), blockSize, encryptedContent)
    fo = open(messageFilename, 'w')
    fo.write(encryptedContent)
    fo.close()
    return encryptedContent


def readFromFileAndDecrypt(messageFilename, keyFilename):
    keySize, n, d = readKeyFile(keyFilename)


    fo = open(messageFilename)
    content = fo.read()
    messageLength, blockSize, encryptedMessage = content.split('_')
    messageLength = int(messageLength)
    blockSize = int(blockSize)

    if keySize < blockSize * 8: # * 8 to convert bytes to bits
        sys.exit('ERROR: Block size is %s bits and key size is %s bits. The RSA cipher requires the block size to be equal to or less than the key size. Did you specify the correct key file and encrypted file?' % (blockSize * 8, keySize))

    encryptedBlocks = []
    for block in encryptedMessage.split(','):
        encryptedBlocks.append(int(block))

    return decryptMessage(encryptedBlocks, messageLength, (n, d), blockSize)

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
# def start():
def start(directory, prikeyfile, pubkeyfile, rnumfile):
    # f=open("rsa_privkey.txt","r")
    f = open(prikeyfile, "r")
    val=f.read()
    f.close()
    res=val.split(",")
    keysize=int(res[0])
    n=int(res[1])

    # f=open("random_file.txt","r")
    f = open(rnumfile, "r")
    rval=f.read()
    f.close()
    res1=rval.split(",")
    rsize=int(res1[0])
    r=int(res1[1])
    G=int(res1[2])

    split = (keysize - rsize) / 8
    # split=(keysize-rsize)/rsize

    # f=open("message.txt","r")
    f = open(directory + "/" + "message.txt", "r")
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
            # XX='0'*(split-len(Xbin))+Xbin
            XX = '0' * ((split * 8) - len(Xbin)) + Xbin
            H=XX[:rsize]
            Y=(int(H,2))^r
            Ybin=bin(Y)[2:]
            YY='0'*(rsize-len(Ybin))+Ybin
            pad_plain=int(XX+YY,2)
            # f=open("msg"+str(i+1)+".txt","w")
            f=open(directory + "/" +"msg"+str(i+1)+".txt","w")
            f.write(str(pad_plain))
            f.close()
            pad_list=pad_list+[0]
            i=i+1
        # f=open("padding_bits.txt","w")
        f=open(directory + "/" + "padding_bits.txt","w")
        for i in pad_list:
            f.write(str(i))
            f.write("\n")
        f.close()
    else:
        # k0=(split-(mlen%split))*rsize
        k0 = (split - (mlen % split)) * 8
        i=0
        while i<mlen/split:
            split_msg=msg[split*i:split*(i+1)]
            M=msg_to_binary(split_msg)
            X=(int(M,2))^G
            Xbin=bin(X)[2:]
            # XX='0'*(split-len(Xbin))+Xbin
            XX = '0' * ((split * 8) - len(Xbin)) + Xbin
            H=XX[:rsize]
            Y=(int(H,2))^r
            Ybin=bin(Y)[2:]
            YY='0'*(rsize-len(Ybin))+Ybin
            pad_plain=int(XX+YY,2)
            # f=open("msg"+str(i+1)+".txt","w")
            f=open(directory+"/"+"msg"+str(i+1)+".txt","w")
            f.write(str(pad_plain))
            f.close()
            pad_list=pad_list+[0]
            i=i+1
        split_msg=msg[split*(mlen/split):]
        M=msg_to_binary(split_msg)
        M=M+'0'*k0
        X=(int(M,2))^G
        Xbin=bin(X)[2:]
        # XX='0'*(split-len(Xbin))+Xbin
        XX = '0' * ((split * 8) - len(Xbin)) + Xbin
        H=XX[:rsize]
        Y=(int(H,2))^r
        Ybin=bin(Y)[2:]
        YY='0'*(rsize-len(Ybin))+Ybin
        pad_plain=int(XX+YY,2)
        # f=open("msgpad.txt","w")
        f=open(directory + "/" + "msgpad.txt","w")
        f.write(str(pad_plain))
        f.close()
        pad_list=pad_list+[k0]
        # f=open("padding_bits.txt","w")
        f=open(directory + "/" + "padding_bits.txt","w")
        for i in pad_list:
            f.write(str(i))
            f.write("\n")
        f.close()

    # main('encrypt')
    main('encrypt', directory, prikeyfile, pubkeyfile)
# def end():
def end(directory, prikeyfile, pubkeyfile, rnumfile):
    # f = open("rsa_privkey.txt", "r")
    f = open(prikeyfile, "r")
    val = f.read()
    f.close()
    res = val.split(",")
    keysize = int(res[0])
    n = int(res[1])

    # f = open("random_file.txt", "r")
    f = open(rnumfile, "r")
    rval = f.read()
    f.close()
    res1 = rval.split(",")
    rsize = int(res1[0])
    r = int(res1[1])
    G = int(res1[2])

    # split = (keysize - rsize) / rsize
    split = (keysize - rsize) / 8
    # main('decrypt')
    main('decrypt', directory, prikeyfile, pubkeyfile)
    # f=open("padding_bits.txt","r")
    f = open(directory + "/" + "padding_bits.txt", "r")
    pad_0_list=map(int,f.readlines())
    f.close()
    for i in range(len(pad_0_list)):
        if i==len(pad_0_list)-1:
            if pad_0_list[-1]==0:
                # filename="msg"+str(i+1)+".txt"
                filename=directory + "/" + "msg"+str(i+1)+".txt"
            else:
                # filename="msgpad.txt"
                filename=directory + "/" + "msgpad.txt"
        else:
            # filename="msg"+str(i+1)+".txt"
            filename=directory + "/" + "msg"+str(i+1)+".txt"
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
        # res=(x*(split/rsize))+x[:(split%rsize)]
        res = (x * ((split * 8) / rsize)) + x[:((split * 8) % rsize)]
        G=int(res,2)
        M=int(X,2)^G
        if k0==0:
            MM=bin(M)[2:]
            # MM='0'*((split*rsize)-len(MM))+MM
            MM = '0' * ((split * 8) - len(MM)) + MM
        else:
            MM=bin(M)[2:-k0]
            # MM='0'*((split*rsize)-k0-len(MM))+MM
            MM = '0' * ((split * 8) - k0 - len(MM)) + MM
        MMM=binary_to_string(MM)
        print MMM
        # filenm="decr"+str(i+1)+".txt"
        filenm=directory + "/" + "decr"+str(i+1)+".txt"
        f=open(filenm,"w")
        f.write(MMM)
        f.close()

    final=""
    for i in range(len(pad_0_list)):
        # filenm="decr"+str(i+1)+".txt"
        filenm=directory + "/" + "decr"+str(i+1)+".txt"
        f=open(filenm,"r")
        s=f.read()
        f.close()
        final=final+s
    # f=open("final_decr.txt","w")
    f=open(directory + "/" + "final_decr.txt","w")
    f.write(final)
    f.close()

# the main() function.
#if __name__ == '__main__':
#    main()
