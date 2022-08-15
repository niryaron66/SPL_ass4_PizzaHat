import sys
from _Repository import repo

arguments=sys.argv[1:4]
config = arguments[0]
order= arguments[1]
output = arguments[2]
config = ''.join([str(elem) for elem in config])
order=''.join([str(elem) for elem in order])
output = ''.join([str(elem) for elem in output])
repo.create_tables()
repo.configDatabase(config)
repo.takeCareOfOrders(order,output)
# repo.close()




