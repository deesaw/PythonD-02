#var args
def total(*args):
	print(sum(args))

total(2,3)
total(2,3,5)
total(2,3,8,9,6,7,4)

#var kwargs

def create_employee(**kwargs):
	print(kwargs)

create_employee(name="hari")
create_employee(name="hari",eid=456)
create_employee(name="hari",eid=456,mobile='988597003')