# %%
import pandas as pd
import numpy as np
import re
# %%
df = pd.read_excel('data/env_tech.xlsx')

# %%
def extend_classes(x):
    exceptions = ["F02M39-71"]
    try:
        results = []
        if isinstance(x, float):
            return np.nan
        if ";" in x:
            x = [str(i) for i in x.split(";")]
        else:
            x = [str(x)]
        for v in x:
            if "-" in v:
                if v in exceptions:
                    upper_class = v[:5]
                    nrange = v[5:]
                else:
                    upper_class = v.split("/")[0]
                    nrange = v.split("/")[1]
                # get digits before "-" and before letter
                start = int(re.findall(r"(\d+)-", nrange)[0])
                end = int(re.findall(r"-(\d+)", nrange)[0])
                assert start < end
                # return two digit strings also for one digit numbers
                range_values = [upper_class + "/" + str(i).zfill(2) for i in range(start, end+1)]
                # remove whitespace
                range_values = [i.replace(" ", "") for i in range_values]
                results.extend(range_values)
            else:
                v = v.replace(" ", "")
                results.append(v)
        return ";".join(results)
    except:
        raise ValueError("Error for value: {}".format(x))
        nrange = v.split("/")[1]
        print(int(re.findall(r"(\d+)-", nrange)[0]))
# %%
extend_classes("F02M39-71")
# %%
df["Extended Classes"] = df["IPC and CPC Classes"]
df["Extended Classes"] = df["Extended Classes"].apply(extend_classes)
# %%
df.to_pickle("data/env_tech.pkl")