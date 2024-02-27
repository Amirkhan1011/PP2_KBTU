import json

with open("sample.json", "r") as file:
    data = json.load(file)



text = """Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------"""
print(text)
for imdata in data["imdata"]:
    for i in imdata:
        for j in imdata[i]: 
            print(imdata[i][j]["dn"],"\t", "\t \t \t", imdata[i][j]["speed"] , imdata[i][j]["mtu"])

