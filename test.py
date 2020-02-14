fileName=["ab:c","def?","ggg/"]

def removeChar():
	global fileName
	tempList=[]
	translation_table = dict.fromkeys(map(ord, '?:/'), None)
	for s in fileName:
		tempList.append(s.translate(translation_table))
	fileName=tempList
	print(fileName)
def removeIllegibleChar(wordToClean):
	translation_table = dict.fromkeys(map(ord, '?:/'), None)
	wordToClean = wordToClean.translate(translation_table)
	print(wordToClean)	

removeIllegibleChar(input("Write word: "))