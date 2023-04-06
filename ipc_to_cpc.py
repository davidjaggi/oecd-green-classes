# %%
import pandas as pd
import xmltodict
import numpy as np
# %%
with open("data/IPCCPC-epoxif-202204.xml","r") as fd:
    cpc_ipc = fd.read()
# %%
cpc_ipc_dict = xmltodict.parse(cpc_ipc)
# %%
cpc_ipc_dict = cpc_ipc_dict["Epoxif"]["Doc"]
# %%
ipc_to_cpc = {}
for item in cpc_ipc_dict:
    field = item["Fld"]
    ipc = field[0]["Prg"]["Sen"]
    ipc_class = ipc["#text"]
    cpc = field[1]["Prg"]["Sen"]
    if type(cpc) == list:
        cpc_class = [c["#text"] for c in cpc]
        cpc_class = [c.replace(" ","").replace(";","") for c in cpc_class]
    else:
        cpc_class = cpc["#text"]
    ipc_to_cpc[ipc_class] = cpc_class
# %%
df_env_tech = pd.read_pickle("data/env_tech.pkl")
# %%
df_env_tech["Green CPC"] = None
# iterate over df_env_tech
for i,v in df_env_tech.iterrows():
    try:
        cpc_classes = []
        if type(v["Extended Classes"]) != str:
            mixed_classes = []
        elif len(v["Extended Classes"]) > 1:
            mixed_classes = v["Extended Classes"].split(";")
        else:
            mixed_classes = v["Extended Classes"]
        for c in mixed_classes:
            if c in ipc_to_cpc.keys():
                cpc_classes.append(ipc_to_cpc[c])
            else:
                cpc_classes.append(c)
        # if list contians lists, flatten it
        if any(isinstance(el, list) for el in cpc_classes):
            cpc_classes = [item for sublist in cpc_classes for item in sublist]
        df_env_tech["Green CPC"][i] = cpc_classes
    except:
        print(i)
# %%
df_env_tech.to_pickle("data/env_tech_cpc.pkl")