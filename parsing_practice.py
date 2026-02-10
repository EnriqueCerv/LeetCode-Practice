# %%
import pandas as pd
from io import StringIO
import re
import json
from collections import Counter

# %%
st = "name,age,city\nAlice,30,New York\nBob,25,LA"

df = pd.read_csv(StringIO(st))
df

# %%

log = "Error at 2025-08-12 14:55:23 - Disk full"
matches = re.findall(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}", log)
timestamps = pd.to_datetime(matches)  # convert to datetime objects
print(timestamps)
# %%
s = '{"data": [{"value": 10}, {"value": 15}]}'
data = json.loads(s)
df = pd.json_normalize(data['data'])
print(df['value'].sum())
# %%
data = "a|b|c#d|e|f#g|h|i"
data = data.split('#')
data = [[char for char in ele.split('|')] for ele in data]
data
# %%

data = "a|b|c#d|e|f#g|h|i"
data = data.replace('#', '\n')
df = pd.read_csv(StringIO(data), sep='|', header=None)
print(df.values.tolist())
# %%

text = "apple banana apple orange banana apple pear"
freq = Counter(text.split())
freq = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))
top_3 = dict(list(freq.items())[:3])
print(top_3)