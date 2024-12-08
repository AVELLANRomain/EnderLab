from layout import Layout
from protocol.protocol import ProtocolRepository, Protocol

from protocol.protocol_creator import create_new_protocol, add_step
import json

# Load layout
layout = Layout()
layout.load(path="data/layout_1.json")
repo = ProtocolRepository(layout=layout)

# create empty protocol
protocol=create_new_protocol(layout)

#load protocol1
protocol1 = repo.get(path="data/elementary_steps/pick_cone.json")

add_step(protocol,protocol1)
# [1,[0,0]]

# #map protocol1
# protocol1.mapping["wells"]["well"]="tips"
# protocol.mapping["wells"]["tips"]=[1,[0,0]]

# #add protocol1
# protocol.steps.append(protocol1)

# #load protocol2
# protocol2 = repo.get(path="data/elementary_steps/mouve_volume.json")

# #map protocol2
# protocol2.mapping["wells"]["well_from"]="from"
# protocol.mapping["wells"]["from"]=[1,[0,1]]
# protocol2.mapping["wells"]["well_to"]="to"
# protocol.mapping["wells"]["to"]=[1,[0,2]]
# protocol2.mapping["params"]["volume"]="volume"
# protocol.mapping["params"]["volume"]=100

# #add protocol2
# protocol.steps.append(protocol2)

dic=protocol.to_dic(protocol)
# save dic
path="test.json"
with open(path, "w") as fp:
        json.dump(dic, fp, indent=2)