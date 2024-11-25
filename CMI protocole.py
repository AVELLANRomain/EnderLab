import json
from protocol_builder import mouve_volume, dispens, serial_dilution

#remplire les eppendorf
dic={"name": "CMI", "actions":[]}

scott25ml=[3,[0,0]]

# antibio from eppendorf:
antibios=[]
i=0
while i<8:
    antibio=[0,[0,i]]
    antibios.append(antibio)
    i+=1

#controle negatif et positif (1er et dernierre colone)
negatifs=[]
positifs=[]
i=0
while i<8:
    negatifs.append([1,[0,i]])
    positifs.append([1,[11,i]])
    i+=1

actions=dispens(scott25ml,negatifs, 200)
dic["actions"].extend(actions)
actions=dispens(scott25ml,positifs, 200)
dic["actions"].extend(actions)

#faire les cmi
atb_vol=10
i=0
x=0
y=1
for antibio in antibios:
    if i==8:
        x=0
        y=6
        
    print(x,y)
    #remplire le 1er puits
    dic["actions"].append(mouve_volume(scott25ml,([1,[x,y]]), 200-atb_vol))
    dic["actions"].append(mouve_volume(antibio,([1,[x,y]]), atb_vol))
    
    #generer la liste de dilution
    wells_to=[]
    j=1
    while j<=4:
        wells_to.append([1,[x,y+j]])
        j+=1
        
    #faire la dilution
    dic["actions"].extend(serial_dilution(scott25ml, [1,[x,y]], wells_to))
    x+=1
    i+=1
    
#save modules
with open('CMI.json', 'w') as fp:
    json.dump(dic, fp, indent=2)