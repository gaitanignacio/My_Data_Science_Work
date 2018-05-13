import MapReduce
import sys

"""
Probelm 4 Solution in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    #key = record[0]
    #value = record[1]
    if record==sorted(record):
    	mr.emit_intermediate(record[0]+" "+record[1],1)
    else:	
    	mr.emit_intermediate(record[1]+" "+record[0],-1)
def reducer(key, list_of_values):
    # key: word
    # value: is a list of the documents names
    key=key.split()
    aux=0
    for x in list_of_values:
	aux += x
    if aux!=0:
    	mr.emit((key))
	mr.emit((key[1],key[0]))
    #elif aux==1:
	#mr.emit((key[1],key[0]))
# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
