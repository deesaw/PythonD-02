from mymodule import FileInfo

f=FileInfo("sample.txt")
f.getsize()
f.linecount()
f.firstline()
f.lastline()
f.nthline(3)
f.search("this")
f.getage()
f.close()

print(dir(f))
help(f.search)