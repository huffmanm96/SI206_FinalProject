import csv
import pickle
from collections import defaultdict

with open('NH_geo_data_1.txt', 'rb') as file1:
  a = pickle.loads(file1.read())
with open('NH_geo_data_2.txt', 'rb') as file2:
  b = pickle.loads(file2.read())
with open('NH_geo_data_3.txt', 'rb') as file3:
  c = pickle.loads(file3.read())

print (len(a))
print (len(b))
print (len(c))

dall = {}
dall.update(a)
dall.update(b)
dall.update(c)

print (len(dall))


    