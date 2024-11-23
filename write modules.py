import json

#remplire les eppendorf
dic={"name": "CMI", "dimension": [6, 6], "max_high": 105, "modules":[]}


#creer le module eppendorf
#creer les wells
i=0
col=[]
xj=8
incrx=14
yi=6
incry=29
while i<4:
    j=0
    raw=[]
    while j<8:
        well={"position": [xj+j*incrx, yi+i*incry], "volume_max": 1500, "volume": 0}
        raw.append(well)
        j+=1
    col.append(raw)
    i+=1
#creer le module  
eppendorf={"name": "eppendorf", "position": [125, 44], "hauteur": 65, "wells": col}
dic["modules"].append(eppendorf.copy())


#module microplaque 96
i=0
col=[]
xi=26
yj=16
incr=9
while i<8:
    j=0
    raw=[]
    while j<12:
        well={"position": [xi+i*incr, yj+j*incr], "volume_max": 200, "volume": 0}
        raw.append(well)
        j+=1
    col.append(raw)
    i+=1
#creer le module  
microplate96={"name": "microplate96", "position": [8, 44], "hauteur": 56, "wells": col}
dic["modules"].append(microplate96.copy())


#module de boite a connes
i=0
col=[]
xj=8 
yi=26.9
incr=9
while i<5:
    j=0
    raw=[]
    while j<12:
        well={"position": [xj+i*incr, yi+j*incr], "volume_max": 56, "volume": 1}# vol max sert de hauteur pou le pick up, vol sert de statue de remplissage (=0 si plus de conne)
        raw.append(well)
        j+=1
    col.append(raw)
    i+=1
#creer le module  
tipsbox={"name": "tipsbox", "position": [125, 44], "hauteur": 48, "wells": col} #set hauteur a 19 une fois etalonner
dic["modules"].append(tipsbox.copy())

#module bouteille scott
well=well={"position": [18, 18], "volume_max": 25000, "volume": 25000}
scott25ml={"name": "scott25ml", "position": [125, 44], "hauteur": 105, "wells": [[well]]}

#save modules
with open('layout.json', 'w') as fp:
    json.dump(dic, fp, indent=2)
