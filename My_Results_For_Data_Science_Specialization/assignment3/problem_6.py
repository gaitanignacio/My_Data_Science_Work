import MapReduce
import sys
#import numpy

"""
Probelm 5 Solution in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    table = record[0]
    if table=="a":
	for k in range(5):
		mr.emit_intermediate((record[1],k),record)
    elif table=="b":
	for k in range(5):
		mr.emit_intermediate((k,record[2]),record)
def reducer(key, list_of_values):
    # key: word
    # value: is a list of the documents names
    a=[0,0,0,0,0]
    b=[0,0,0,0,0]
    result=0
    for values in list_of_values:
	if values[0]=='a':
		a[values[2]]=values[3]
	elif values[0]=='b':
		b[values[1]]=values[3]
    result = sum(i*j for i,j in zip(a,b))
    mr.emit((key[0],key[1],result))
# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
