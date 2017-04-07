import os
import io
from PIL import Image
from array import array

def readimage(path):
    #count = os.stat(path).st_size / 2
    with open(path, "rb") as f:
        return bytearray(f.read())

##bytes = readimage("BFS.png")
##image = Image.open(io.BytesIO(bytes))
##image.save("BFSCOPY.png")


##with open("test.xlsx",'rb') as f:
##    g=io.BytesIO(f.read())   ## Getting an Excel File represented as a BytesIO Object
g= readimage("samplepdf.pdf")
temporarylocation="testoutpdf.pdf"
with open(temporarylocation,'wb') as out: ## Open temporary file as bytes
    out.write(g)
