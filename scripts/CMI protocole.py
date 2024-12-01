import json

from scripts.protocol_builder import mix, mouve_volume, serial_dilution

# remplire les eppendorf
dic = {"name": "CMI", "actions": []}
atb_vol = 10
scott25ml = [3, [0, 0]]

# antibio from eppendorf:
antibios = []
i = 0
while i < 8:
    antibio = [0, [0, i]]
    antibios.append(antibio)
    i += 1


# controle negatif et positif (1er et dernierre colone)
negatifs = []
positifs = []
i = 0
while i < 8:
    negatifs.append([1, [i, 0]])
    positifs.append([1, [i, 11]])
    i += 1

# actions=dispens(scott25ml,negatifs, 200)
# dic["actions"].extend(actions)
# actions=dispens(scott25ml,positifs, 200)
# dic["actions"].extend(actions)

# faire les cmi
i = 0
x = 0
y = 1
for antibio in antibios:
    if i == 8:
        x = 0
        y = 6

    print(x, y)
    # remplire le 1er puits
    dic["actions"].append(mouve_volume(scott25ml, ([1, [x, y]]), 200 - atb_vol))
    dic["actions"].append(mouve_volume(antibio, ([1, [x, y]]), atb_vol))
    dic["actions"].append(mix(([1, [x, y]]), 100, 2))
    # change tips

    # generer la liste de dilution
    wells_to = []
    j = 1
    while j <= 4:
        wells_to.append([1, [x, y + j]])
        j += 1

    # faire la dilution
    dic["actions"].extend(serial_dilution(scott25ml, [1, [x, y]], wells_to))
    x += 1
    i += 1

# save modules
with open("data/CMI.json", "w") as fp:
    json.dump(dic, fp, indent=2)
