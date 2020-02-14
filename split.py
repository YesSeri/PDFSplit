from PyPDF2 import PdfFileWriter, PdfFileReader
import os

startNumber=[]
endNumber=[]
fileName=[]

def main():

	importNumberPageSplit()
	importName()
	splitPdf()


def importNumberPageSplit():
	f=open("whichPageNumber/pagesFile.txt", "r")
	if f.mode == 'r':
		contents =f.read().strip()
		f.close() 
		data = contents.split("|")
		for y in data:
			wordSplit=y.split("-")
			startNumber.append(int(wordSplit[0]))
			endNumber.append(int(wordSplit[1]))
	else:
		print("could not read text file")

def importName():
	with open("whichPageNumber/nameFile.txt", "r") as f:
		contents =f.read().strip()
		f.close()
		global fileName
		fileName=contents.split("|")
		for i in range(len(fileName)):
			fileName[i]+='.pdf'

def splitPdf():
	newFolderName = input("name of output folder: ")
	if not os.path.exists(newFolderName):
		os.makedirs(newFolderName)

	pdfName=input("name of pdf in pdfsToSplit: ")

	inputpdf = PdfFileReader(open(f"pdfsToSplit/{pdfName}", "rb"))

	for x in range(len(startNumber)):
		output = PdfFileWriter()
		for i in range(endNumber[x] - startNumber[x]+1):
			output.addPage(inputpdf.getPage(i+startNumber[x]-1))
		with open(newFolderName + "/" + fileName[x], "wb") as outputStream:
			output.write(outputStream)	

main()