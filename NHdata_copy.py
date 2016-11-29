import csv
import json
import pickle
from collections import defaultdict

with open('/Users/maddiehuffman/Desktop/NH_Geocodes/NH_Geocodes/NH_50m/NH_geo_data_1.txt', 'rb') as file1:
  a = pickle.loads(file1.read())
with open('/Users/maddiehuffman/Desktop/NH_Geocodes/NH_Geocodes/NH_50m/NH_geo_data_2.txt', 'rb') as file2:
  b = pickle.loads(file2.read())
with open('/Users/maddiehuffman/Desktop/NH_Geocodes/NH_Geocodes/NH_50m/NH_geo_data_3.txt', 'rb') as file3:
  c = pickle.loads(file3.read())

##print (len(a))
##print (len(b))
##print (len(c))

fifty = {}
fifty.update(a)
fifty.update(b)
fifty.update(c)

fieldnames = []
for item in fifty.keys():
    fieldnames.append(item)
    
rows = zip(fifty.values())

with open('NHgeo_50m.csv', 'w') as f:  # Just use 'w' mode in 3.x
    w = csv.DictWriter(f, fifty.keys())
    w.writeheader()

with open('NHgeo_50m.csv', 'a') as g:  # Just use 'w' mode in 3.x
    writer = csv.writer(g)
    for row in rows:
        writer.writerow(row)




print ("Length of 50m dictionary is " + str(len(fifty)))


    
with open('/Users/maddiehuffman/Desktop/NH_Geocodes/NH_Geocodes/NH_40m/NH_geo_data_1.txt', 'rb') as file4:
  d = pickle.loads(file4.read())
with open('/Users/maddiehuffman/Desktop/NH_Geocodes/NH_Geocodes/NH_40m/NH_geo_data_2.txt', 'rb') as file5:
  e = pickle.loads(file5.read())
with open('/Users/maddiehuffman/Desktop/NH_Geocodes/NH_Geocodes/NH_40m/NH_geo_data_3.txt', 'rb') as file6:
  f = pickle.loads(file6.read())

fourty = {}
fourty.update(d)
fourty.update(e)
fourty.update(f)

print ("Length of 40m dictionary is " + str(len(fourty)))



with open('/Users/maddiehuffman/Desktop/NH_Geocodes/NH_Geocodes/NH_30m/NH_geo_data_1.txt', 'rb') as file7:
  g = pickle.loads(file7.read())
with open('/Users/maddiehuffman/Desktop/NH_Geocodes/NH_Geocodes/NH_30m/NH_geo_data_2.txt', 'rb') as file8:
  h = pickle.loads(file8.read())
with open('/Users/maddiehuffman/Desktop/NH_Geocodes/NH_Geocodes/NH_30m/NH_geo_data_3.txt', 'rb') as file9:
  i = pickle.loads(file9.read())

thirty = {}
thirty.update(g)
thirty.update(h)
thirty.update(i)

print ("Length of 30m dictionary is " + str(len(thirty)))



