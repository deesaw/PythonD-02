ips = [
"www.google.com",
"www.intel.com",
"localhost",
"127.0.0.1",
"www.deloittepythonrameshhyd.com"
]

def isup(ip):
	return True

for ip in ips:
	if isup(ip):
		print("{} is up".format(ip))
	else:
		print("{} is down".format(ip))