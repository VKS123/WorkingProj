import os
from tkFileDialog import askopenfilename
from Tkinter import *
from rsaKeyGeneration import *
from r_generation_file import *
from file_encrpty_decrypt import *
from rsaCipher_combine import *
import zipfile
file_path=''

def open_file(entry):
    global file_path
    filename = askopenfilename()
    file_path = filename
    entry.delete(0, END)
    entry.insert(0, file_path)
    file_path=''

def decryption_window():
    close_main()
    global decrptwindow
    global entry4
    global entry5
    global entry6
    global entry8
    global l3,l8,l9
    global df3,df1
    decrptwindow = Tk()
    decrptwindow.title('')
    decrptwindow.geometry()
    df=Frame(decrptwindow)
    df.pack()
    df1 = Frame(df, width=300, height=150)
    df1.pack(fill=X)
    # df2 = Frame(df, width=300, height=150)
    # df2.pack()
    df3 = Frame(df, highlightbackground="green", highlightcolor="green", highlightthickness=3, width=1000, height=1000)
    df3.pack()
    l8 = Label(df3, text="Please fill in the input fields to generate the Decryption")
    l8.place(relx=0.5, rely=0.4, anchor=CENTER)
    l9 = Label(df3, text="FLOW CHART")
    l9.place(relx=0.5, rely=0.5, anchor=CENTER)
    Label(df1, text="Select private key file").grid(row=0, column=1, sticky='e')
    Label(df1, text="Select public key file").grid(row=1, column=1, sticky='e')
    Label(df1, text="Select random number file").grid(row=2, column=1, sticky='e')
    Label(df1, text="Select file to decrypt").grid(row=3, column=1, sticky='e')
    l3 = Label(df1)
    l3.grid(row=4, column=5, sticky='we')
    entry4 = Entry(df1, width=50, textvariable=file_path)
    entry4.grid(row=0, column=2, padx=2, pady=2, sticky='we', columnspan=25)
    entry5 = Entry(df1, width=50, textvariable=file_path)
    entry5.grid(row=1, column=2, padx=2, pady=2, sticky='we', columnspan=25)
    entry6 = Entry(df1, width=50, textvariable=file_path)
    entry6.grid(row=2, column=2, padx=2, pady=2, sticky='we', columnspan=25)
    entry8 = Entry(df1, width=50, textvariable=file_path)
    entry8.grid(row=3, column=2, padx=2, pady=2, sticky='we', columnspan=25)
    Button(df1, text="Browse", command=lambda: open_file(entry4)).grid(row=0, column=27, sticky='ew', padx=8, pady=4)
    Button(df1, text="Browse", command=lambda: open_file(entry5)).grid(row=1, column=27, sticky='ew', padx=8, pady=4)
    Button(df1, text="Browse", command=lambda: open_file(entry6)).grid(row=2, column=27, sticky='ew', padx=8, pady=4)
    Button(df1, text="Browse", command=lambda: open_file(entry8)).grid(row=3, column=27, sticky='ew', padx=8, pady=4)
    Button(df1, text="Flow diagram", command=lambda: create_window(df1,"img2.png","img4.png")).place(relx=0.8, rely=0.2)
    Button(df1, text="Decrypt", command=decrypt).grid(row=5, column=0, sticky='we', padx=8, pady=4)
    Button(df1, text="Back", command=close_decryption_window).grid(row=5, column=2, sticky='we', padx=8, pady=4)

def create_window(f,i1,i2):
    window = Toplevel(f)
    logo_filepath = i1
    img = PhotoImage(file=logo_filepath)
    img = img.subsample(1)
    logo = Label(window, image=img)
    logo.photo = img
    logo.grid(row=50, column=0, rowspan=550, columnspan=250)
    logo_filepath1 = i2
    img1 = PhotoImage(file=logo_filepath1)
    img1 = img1.subsample(4,5)
    logo1 = Label(window, image=img1)
    logo1.photo = img1
    logo1.grid(row=0, column=262, rowspan=550, columnspan=250)

def encryption_window():
    close_main()
    global encrptwindow
    global entry1
    global entry2
    global entry3
    global entry7
    global l2,l6,l7
    global ef1,ef3
    encrptwindow = Tk()
    encrptwindow.title('')
    encrptwindow.geometry()
    ef=Frame(encrptwindow)
    ef.pack()
    ef1 = Frame(ef, width=300, height=150)
    ef1.pack(fill=X)
    # ef2 = Frame(ef, width=300, height=150)
    # ef2.pack()
    ef3 = Frame(ef, highlightbackground="green", highlightcolor="green", highlightthickness=3, width=1000, height=1000)
    ef3.pack()
    l6 = Label(ef3, text="Please fill in the input fields to generate the Encrypion")
    l6.place(relx=0.5, rely=0.4, anchor=CENTER)
    l7 = Label(ef3, text="FLOW CHART")
    l7.place(relx=0.5, rely=0.5, anchor=CENTER)
    Label(ef1, text="Select private key file").grid(row=0, column=1, sticky='e')
    Label(ef1, text="Select public key file").grid(row=1, column=1, sticky='e')
    Label(ef1, text="Select random number file").grid(row=2, column=1, sticky='e')
    Label(ef1, text="Select file to encrypt").grid(row=3, column=1, sticky='e')
    l2 = Label(ef1)
    l2.grid(row=4, column=5, sticky='we')
    entry1 = Entry(ef1, width=50, textvariable=file_path)
    entry1.grid(row=0, column=2, padx=2, pady=2, sticky='we', columnspan=25)
    entry2 = Entry(ef1, width=50, textvariable=file_path)
    entry2.grid(row=1, column=2, padx=2, pady=2, sticky='we', columnspan=25)
    entry3 = Entry(ef1, width=50, textvariable=file_path)
    entry3.grid(row=2, column=2, padx=2, pady=2, sticky='we', columnspan=25)
    entry7 = Entry(ef1, width=50, textvariable=file_path)
    entry7.grid(row=3, column=2, padx=2, pady=2, sticky='we', columnspan=25)
    Button(ef1, text="Browse", command=lambda: open_file(entry1)).grid(row=0, column=27, sticky='ew', padx=8, pady=4)
    Button(ef1, text="Browse", command=lambda: open_file(entry2)).grid(row=1, column=27, sticky='ew', padx=8, pady=4)
    Button(ef1, text="Browse", command=lambda: open_file(entry3)).grid(row=2, column=27, sticky='ew', padx=8, pady=4)
    Button(ef1, text="Browse", command=lambda: open_file(entry7)).grid(row=3, column=27, sticky='ew', padx=8, pady=4)
    Button(ef1, text="Flow diagram", command=lambda: create_window(ef1,"img2.png","img3.png")).place(relx=0.8,rely=0.2)
    Button(ef1, text="Encrypt", command=encrypt).grid(row=5, column=0, sticky='we', padx=8, pady=4)
    Button(ef1, text="Back",  command=close_encryption_window).grid(row=5, column=2, sticky='we', padx=8, pady=4)


def generate_keys_window():
    close_main()
    global keywindow
    global e1
    global e2
    global l1,l4,l5
    global f3
    keywindow = Tk()
    keywindow.title('')
    keywindow.geometry()
    kf=Frame(keywindow)
    kf.pack()
    f1 = Frame(kf, width=300, height=150)
    f1.pack(fill=X)
    # f2 = Frame(kf, width=300, height=150)
    # f2.pack()
    f3 = Frame(kf, highlightbackground="green", highlightcolor="green", highlightthickness=3,width=1000, height=1000)
    f3.pack()
    l4=Label(f3, text="Please fill in the input fields to generate the Key Generation")
    l4.place(relx=0.5, rely=0.4, anchor=CENTER)
    l5 = Label(f3, text="FLOW CHART")
    l5.place(relx=0.5, rely=0.5, anchor=CENTER)
    Label(f1, text="Key size :-").grid(row=1, column=3, sticky='e', padx=10, pady=4)
    Label(f1, text="Random number r size :-").grid(row=2, column=3, sticky='e', padx=10, pady=4)
    l1=Label(f1)
    l1.grid(row=3, column=4, sticky='we')
    e1 = Entry(f1)
    e1.grid(row=1, column=4, padx=2, pady=2, sticky='we')
    e2 = Entry(f1)
    e2.grid(row=2, column=4, padx=2, pady=2, sticky='we')

    # logo_filepath = "img1.png"
    # img = PhotoImage(file=logo_filepath)
    # img = img.subsample(2,2)
    # logo = Label(f2, image=img)
    # logo.photo = img
    # logo.grid(row=0, column=0, rowspan=550, columnspan=250)
    Button(f1, text="Generate", width=12, command=generate_keys).grid(row=4, column=0, sticky='we', padx=8, pady=4)
    Button(f1, text="Back", width=12, command=close_generate_keys_window).grid(row=4, column=1, sticky='we', padx=8, pady=4)


def encrypt():
    content = [
        ' Generating prime number P and Q of keysize bits',
        '|',
        ' Rabin Miller algo to confirm the number is prime',
        '|',
        ' Compute n= p * q',
        '|',
        ' Compute phi( n ) = ( p - 1 ) * ( q - 1 )',
        '|',
        ' Select e : GCD( e , phi( n ) ) = 1',
        '|',
        ' Select d: d * e = 1 mod phi( n ) and d < phi( n )',
        '|',
        ' Public Key : - n , e ',
        '|',
        ' Private Key : - n , d ',
        '|',
        '  Generating prime number R of rsize bits',
    ]
    example = [
        ' Let P = 15 and Q = 11 keysize = 4',
        '|',
        ' Rabin Miller algo verified P and Q is prime',
        '|',
        ' n = 15 * 11 => n = 165 ',
        '|',
        ' phi( n ) = ( 15 - 1 ) * ( 11 - 1 ) => phi(n) = 140',
        '|',
        ' e : GCD( e , 140 ) = 1  =>  e = 9',
        '|',
        ' d: d * 9 = 1 mod 140 and d < 140 => d = 23',
        '|',
        ' Public Key : - 165 , 9 ',
        '|',
        ' Private Key : - 165 , 23 ',
        '|',
        '  R = 3 rsize = 2',
    ]
    if len(entry1.get())==0 or len(entry2.get())==0 or len(entry3.get())==0 or len(entry7.get())==0:
        l2.config(text="Please provide all inputs")
    else:
        l6.destroy()
        l7.destroy()
        for i in range(len(content)):
            encrptwindow.after(i * 500, flowchart, ef3,content[i].center(50), i, 0.3)
        for i in range(len(example)):
            encrptwindow.after(i * 500, flowchart, ef3,example[i].center(50), i, 0.7)
        # print entry1.get()
        # print entry2.get()
        # print entry3.get()
        # print entry7.get().split("/")[-1]
        fn=entry7.get().split("/")[-1]
        directory=enc(fn)
        f=open(directory+"/extension.txt","w")
        f.write(fn.split(".")[-1])
        f.close()
        start(directory,entry1.get(),entry2.get(),entry3.get())



def decrypt():
    content = [
        ' Generating prime number P and Q of keysize bits',
        '|',
        ' Rabin Miller algo to confirm the number is prime',
        '|',
        ' Compute n= p * q',
        '|',
        ' Compute phi( n ) = ( p - 1 ) * ( q - 1 )',
        '|',
        ' Select e : GCD( e , phi( n ) ) = 1',
        '|',
        ' Select d: d * e = 1 mod phi( n ) and d < phi( n )',
        '|',
        ' Public Key : - n , e ',
        '|',
        ' Private Key : - n , d ',
        '|',
        '  Generating prime number R of rsize bits',
    ]
    example = [
        ' Let P = 15 and Q = 11 keysize = 4',
        '|',
        ' Rabin Miller algo verified P and Q is prime',
        '|',
        ' n = 15 * 11 => n = 165 ',
        '|',
        ' phi( n ) = ( 15 - 1 ) * ( 11 - 1 ) => phi(n) = 140',
        '|',
        ' e : GCD( e , 140 ) = 1  =>  e = 9',
        '|',
        ' d: d * 9 = 1 mod 140 and d < 140 => d = 23',
        '|',
        ' Public Key : - 165 , 9 ',
        '|',
        ' Private Key : - 165 , 23 ',
        '|',
        '  R = 3 rsize = 2',
    ]
    if len(entry4.get())==0 or len(entry5.get())==0 or len(entry6.get())==0 or len(entry8.get())==0:
        l3.config(text="Please provide all inputs")
    else:
        l8.destroy()
        l9.destroy()
        for i in range(len(content)):
            decrptwindow.after(i * 500, flowchart, df3,content[i].center(50), i, 0.3)
        for i in range(len(example)):
            decrptwindow.after(i * 500, flowchart, df3,example[i].center(50), i, 0.7)
        # print entry4.get()
        # print entry5.get()
        # print entry6.get()
        # print entry8.get().split("/")[-1]

        filenam=entry8.get().split("/")
        directory=filenam[-1].split(".")[0]
        zip_ref = zipfile.ZipFile(filenam[-1])
        if not os.path.exists(directory):
            os.makedirs(directory)
        zip_ref.extractall(directory)
        zip_ref.close()
        end(directory,entry4.get(),entry5.get(),entry6.get())
        f=open(directory+"/extension.txt","r")
        extension=f.read()
        f.close()
        dec(directory+"/final_decr.txt",extension)

def flowchart(f,t,r,c):
    a=Label(f, text=t)
    # a.grid(row=r, column=0, sticky='e')
    a.place(relx=c, rely=(r+1)*0.05, anchor=CENTER)

def generate_keys():
    content=[
        ' Generating prime number P and Q of keysize bits',
        '↓',
        ' Rabin Miller algorithm to confirm the numbers P and Q are prime',
        '↓',
        ' Compute the RSA modulus n=p*q',
        '↓',
        ' Compute the Euler\'s totient function Φ(n) = (p-1)*(q-1)',
        '↓',
        ' Select the public exponent e : GCD(e, Φ(n)) = 1',
        '↓',
        ' Select the private exponent d : d*e = 1 mod Φ(n) and d < Φ(n)',
        '↓',
        ' Public Key : - n , e ',
        '↓',
        ' Private Key : - n , d ',
        '↓',
        ' Generating prime number R of rsize bits',
    ]
    example=[
        ' Let P = 15 and Q = 11, keysize = 4',
        '↓',
        ' Rabin Miller algorithm verifies that P and Q are prime',
        '↓',
        ' n = 15 * 11 => n = 165 ',
        '↓',
        ' Φ(n) = (15 - 1) * (11 - 1) => Φ(n) = 140',
        '↓',
        ' e : GCD(e, 140) = 1  =>  e = 9',
        '↓',
        ' d : d*9 = 1 mod 140 and d < 140 => d = 23',
        '↓',
        ' Public Key : - 165, 9 ',
        '↓',
        ' Private Key : - 165, 23 ',
        '↓',
        ' R = 3 rsize = 2',
    ]
    if len(e1.get())==0 or len(e2.get())==0:
        l1.config(text="Please provide all inputs")
    else:
        l4.destroy()
        l5.destroy()
        for i in range(len(content)):
            keywindow.after(i*500,flowchart,f3,content[i].center(50 ),i,0.3)
        for i in range(len(example)):
            keywindow.after(i*500,flowchart,f3,example[i].center(50 ),i,0.7)
        res = makeKeyFiles('rsa', int(e1.get()))
        if len(res):
            l1.config(text=res)
        else:
            r_num_generator(int(e2.get()))
            l1.config(text="The public key, private key and the random number R are generated.")

def close_decryption_window():
    decrptwindow.destroy()
    main()


def close_encryption_window():
    encrptwindow.destroy()
    main()


def close_generate_keys_window():
    keywindow.destroy()
    main()


def close_main():
    root.destroy()


def main():
    global root
    root = Tk()
    root.title('')
    root.geometry()
    mf = Frame(root)
    mf.pack()

    f2 = Frame(mf, width=300, height=10)
    f2.pack()
    f3 = Frame(mf, width=300, height=10)
    f3.pack()
    Button(f2, text="Key Generation", command=generate_keys_window).grid(row=0, column=27, sticky='ew', padx=38, pady=24)
    Button(f2, text="Encryption", command=encryption_window).grid(row=0, column=54, sticky='ew', padx=38, pady=24)
    Button(f2, text="Decryption", command=decryption_window).grid(row=0, column=81, sticky='ew', padx=38, pady=24)
    logo_filepath = "sasa.png"
    img = PhotoImage(file=logo_filepath)
    img = img.subsample(5)
    panel1 = Label(f3, image=img)
    panel1.photo = img
    panel1.grid(row=0, column=0, columnspan=2, rowspan=2, sticky=W + E + N + S, padx=5, pady=5)
    logo_filepath1 = "vid.png"
    img1 = PhotoImage(file=logo_filepath1)
    img1 = img1.subsample(6)

    panel2 = Label(f3, image=img1)
    panel2.photo = img1
    panel2.grid(row=0, column=55, columnspan=2, rowspan=2, sticky=W + E + N + S, padx=5, pady=5)

    logo_filepath2 = "selva.png"
    img2 = PhotoImage(file=logo_filepath2)
    img2 = img2.subsample(2)
    panel3 = Label(f3, image=img2)
    panel3.photo = img2
    panel3.grid(row=0, column=110, columnspan=2, rowspan=2, sticky=W + E + N + S, padx=5, pady=5)
    root.mainloop()
main()

