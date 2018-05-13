import MapReduce
import sys

"""
Probelm 5 Solution in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]
    trimed_dna=value[:-10]
    mr.emit_intermediate(trimed_dna,1)
def reducer(key, list_of_values):
    # key: word
    # value: is a list of the documents names
    mr.emit((key))
# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
