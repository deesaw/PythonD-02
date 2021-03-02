import filecmp
from mymodule import FileInfo

class NewFileInfo(FileInfo):
	def issameasfile(self, filetocompare):
		if filecmp.cmp(self.filename, filetocompare):
			print(f"{self.filename} and {filetocompare} are same")
		else:
			print(f"{self.filename} and {filetocompare} are not same")
	
f=NewFileInfo("sample.txt")
f.getsize()
f.linecount()
f.firstline()
f.lastline()
f.nthline(3)
f.search("this")
f.getage()
f.issameasfile("samp.txt")
f.close()