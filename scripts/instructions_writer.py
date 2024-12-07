import json


with open("../data/mix.json") as json_data:
    d = json.load(json_data)
    
# d["param"]["number"]=10
# d["param"]["vol"]=200
# d["wells"]["well 1"]=[0,[0,1]]


def write_instructions(protocol):

    if protocol["elementary"]==1:
        for action in protocol["actions"]:            
            match action["name"]:
                
                        case "mix":
                            action["well_index"]=protocol["wells"][action["well_index"]]
                            action["volume"]=protocol["param"][action["volume"]]
                            action["number"]=protocol["param"][action["number"]]
    else:
        
        for action in protocol["actions"]:
            #faire le mapping
            for param in action["param"].items():
                print(param)
                print(action["param"][param[0]])
                print(protocol["param"][param[0]])
                action["param"][param[0]]=protocol["param"][param[0]]
                
                write_instructions(action)
            
                    
write_instructions(d)
with open("../data/mix_instructions.json", "w") as fp:
    json.dump(d, fp, indent=2)
