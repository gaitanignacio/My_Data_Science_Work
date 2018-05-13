import MapReduce
import sys

"""
Probelm 1 Solution in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]
    words = value.split()
    for w in words:
      mr.emit_intermediate(w,key)

def reducer(key, list_of_values):
    # key: word
    # value: is a list of the documents names
    document_id_list = []
    for x in list_of_values:
    	if x not in document_id_list:
        	document_id_list.append(x)
    mr.emit((key,document_id_list))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
