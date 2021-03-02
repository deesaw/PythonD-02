import os
import glob
import zipfile

home    = "/Users/sr/Desktop/deloitte"
pattern = "*.py"
target  = "/Users/sr/Desktop/day3.zip"

os.chdir(home)
files2bezipped = glob.glob(pattern)
z = zipfile.ZipFile(target,"w",zipfile.ZIP_DEFLATED)
totalsize=0
for myfile in files2bezipped:
	z.write(myfile)
	totalsize+=os.path.getsize(myfile)
	print(f"Adding {myfile}({os.path.getsize(myfile)})")
	
	
z.close()
print(f"Size of original files  = {totalsize}")
print(f"Zipfile size = {os.path.getsize(target)}")	
print(f"Compression ratio = {round(os.path.getsize(target)/totalsize,2)}")
