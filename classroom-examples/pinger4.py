from mymodule import get_ips_from_file
from simpleping import isup

for ip in get_ips_from_file("ips.txt"):
	if isup(ip):
		print("{} is up".format(ip))
	else:
		print("{} is down".format(ip))
