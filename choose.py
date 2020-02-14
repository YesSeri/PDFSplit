import os
numberOfDocs=0
def main():
	startOrNot=input("Do you want to start? (y to start) ")
	if startOrNot == "y":
		if not os.path.exists("/home/henke/python/pdfSplit/whichPageNumber/"):
			os.makedirs("/home/henke/python/pdfSplit/whichPageNumber/")
		deleteText()
		while True:
			global numberOfDocs
			nameOfFile=input("\nDoc " + str(numberOfDocs) + " name: (0 to end) ")
			nameOfFile = removeIllegibleChar(nameOfFile)
			if nameOfFile=="0":
				break
			
			splittedDocName(nameOfFile)
			numberOfDocs+= 1
 
			start = "a"
			end = "a"

			while not start.isdigit() or not end.isdigit():
				start = input("Start: ")
				end = input("End: ")
			choosePages(start,end)

		deleteLastChar("whichPageNumber/pagesFile.txt")
		deleteLastChar("whichPageNumber/nameFile.txt")
	else:
		print("program quit")

def removeIllegibleChar(wordToClean):
	translation_table = dict.fromkeys(map(ord, '?:/'), None)
	wordToClean = wordToClean.translate(translation_table)
	print (wordToClean)
	return wordToClean	

def deleteText():

	with open("whichPageNumber/nameFile.txt", "w+") as f:
		f.seek(0, os.SEEK_END)
		f.truncate()
	with open("whichPageNumber/pagesFile.txt", "w+") as f:
		f.seek(0, os.SEEK_END)
		f.truncate()

def choosePages(start, end):
	f=open("whichPageNumber/pagesFile.txt", "a+")
	if f.mode == 'a+':
		f.write(f"{start}-{end}|")
		f.close()

def deleteLastChar(nameOfFilePath):
	with open(nameOfFilePath, 'rb+') as f:
	    f.seek(-1, os.SEEK_END)
	    f.truncate()

def splittedDocName(nameOfFile):
	g=open("whichPageNumber/nameFile.txt", "a+")
	if g.mode == 'a+':
		g.write(str(numberOfDocs)+". "+nameOfFile+"|")
		g.close()
main()