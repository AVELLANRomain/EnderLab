import json

#remplire les eppendorf
dic={"name": "alliquot", "actions":[]}


volume=200

i=0
while i<1:
    j=0
    while j<7:
        action={"name": "load","module": 3,"well_index": [0,0],"volume": volume}
        dic["actions"].append(action.copy())
        action={"name": "drop","module": 0,"well_index": [i,j],"volume": volume}
        dic["actions"].append(action.copy())
        j+=1
    i+=1
    
#save modules
with open('alliquot.json', 'w') as fp:
    json.dump(dic, fp, indent=2)