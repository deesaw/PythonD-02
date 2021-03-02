def isup(ip):
	return True


f=open("ips.txt","r")
ips=[]
for line in f:
	ips.append(line.strip())
f.close()


for ip in ips:
	if isup(ip):
		print("{} is up".format(ip))
	else:
		print("{} is down".format(ip))
