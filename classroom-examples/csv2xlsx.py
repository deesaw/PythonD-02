import csv
from openpyxl import Workbook
inputfile = "marks.csv"
outputfile = "marks.xlsx"

wb = Workbook()
ws = wb.active
ws.title = "Marks"

f=open(inputfile,'r')
for row,data in enumerate(csv.reader(f)):
	for col,cell in enumerate(data):
		ws.cell(row = row + 1, column = col + 1,value = cell)
f.close()
wb.save(outputfile)