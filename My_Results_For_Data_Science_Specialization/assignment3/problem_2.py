import MapReduce
import sys

"""
Probelm 2 Solution in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    #key = record[0]
    #value = record[1]
    mr.emit_intermediate(record[1],record)

def reducer(key, list_of_values):
    # key: word
    # value: is a list of the documents names 
    joined_table=[]
    for x in list_of_values:
	if x[0]=="order":
		for y in list_of_values:
			if y[0]=="line_item":
				joined_table.append(x+y)
    for z in joined_table:
	mr.emit((z))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
