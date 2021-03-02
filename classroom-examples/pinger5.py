from mymodule import get_ips_from_xlsx
from simpleping import isup

for ip in get_ips_from_xlsx("ips.xlsx"):
	if isup(ip):
		print("{} is up".format(ip))
	else:
		print("{} is down".format(ip))
