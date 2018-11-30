
import json

f = open("statistic_data_2.json", "r")
imp = f.read()
#print(imp)
#print(type(data),data)
data = json.dumps(imp)
print(type(data))
data = json.loads(data)
#p = data.get('id')
#data = str(data)
#data = dict(data)
#data = data.get('id')

print(type(data),data)
#print(p)
#for line in f:
    #print(line['id'])





f.close()