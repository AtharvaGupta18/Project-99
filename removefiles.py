import os
import shutil
import time

def main():
	foldersDeleted = 0
	filesDeleted = 0

	path = input("Enter the path to folder :- ")
	days = 0.01

	seconds = time.time() - (days * 24 * 60 * 60)

	if os.path.exists(path):
		for rootFolder, folders, files in os.walk(path):
			if seconds >= getAge(rootFolder):
				removeFolder(rootFolder)
				foldersDeleted += 1
			else:
				for folder in folders:
					folderPath = os.path.join(rootFolder, folder)
					if seconds >= getAge(folderPath):
						removeFolder(folderPath)
						foldersDeleted += 1

				for file in files:
					filePath = os.path.join(rootFolder, file)
					if seconds >= getAge(filePath):
						removeFile(filePath)
						filesDeleted += 1
		else:
			if seconds >= getAge(path):
				removeFile(path)
				filesDeleted += 1

	else:
		print("Not found")

def removeFolder(path):
	if not shutil.rmtree(path):
		print("Removed successfully")
	else:
		print("Unable to delete "+path)



def removeFile(path):
	if not os.remove(path):
		print("Removed successfully")

	else:
		print("Unable to delete "+path)


def getAge(path):
	ctime = os.stat(path).st_ctime
	return ctime

if __name__ == '__main__' :
	main()