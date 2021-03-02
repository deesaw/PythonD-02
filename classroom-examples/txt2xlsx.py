import csv
from openpyxl import Workbook
inputfile = "ips.txt"
outputfile = "ips.xlsx"

wb = Workbook()
ws = wb.active

with open(inputfile,'r') as f:
	for ip in f:
		ws.append([ip.strip()])
wb.save(outputfile)