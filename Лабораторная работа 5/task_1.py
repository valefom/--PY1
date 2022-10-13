# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint
pprint([{'bin':bin(x), 'dec':x, 'hex':hex(x), 'oct':oct(x)} for x in range(16)])
