from mymodule import get_ips_from_xlsx
from simpleping import isup



print(list(map(lambda x:(x,isup(x)),get_ips_from_xlsx("ips.xlsx")[:10])))
