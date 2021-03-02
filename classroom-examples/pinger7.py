from mymodule import get_ips_from_db
from simpleping import isup

for ip in get_ips_from_db(database="mydatabase.db",tablename="ips"):
	if isup(ip):
		print("{} is up".format(ip))
	else:
		print("{} is down".format(ip))
