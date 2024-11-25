import json
indexmodule=0
indexwell=[0,0]
well_adress=[indexmodule, indexwell]

def mouve_volume(well_from, well_to, volume):
    action={"name": "move_volume",
            "module_from": well_from[0],
            "well_index_from": well_from[1],
            "module_to": well_to[0],
            "well_index_to": well_to[1],
            "volume": volume}# remplire la 1er colonne
    return action

def dispens(well_from, wells_to, volume):
    actions=[]
    for well_to in wells_to:
        action=mouve_volume(well_from, well_to, volume)
        actions.append(action.copy())
    return actions

def serial_dilution(solvent_well, well_from, wells_to):
    actions=[]
    
    actions.extend(dispens(solvent_well, wells_to, 100))
    
    actions.append(mouve_volume(well_from, wells_to[0], 100))
    actions.append(mouve_volume(solvent_well, well_from, 100))
    
    i=0
    while i<len(wells_to)-1:
        actions.append(mouve_volume(solvent_well, wells_to[i], 100))
        actions.append(mouve_volume(wells_to[i], wells_to[i+1], 100))
        
        i+=1     
    actions.append(mouve_volume(wells_to[-1], [4,[0,0]], 100))  
    return actions
        
    