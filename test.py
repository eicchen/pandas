import pandas as pd
import numpy as np

df1 = pd.DataFrame()
df2 = pd.DataFrame()
df1["t"] = np.array([1721088000012322083, 1721088047408560273, 1721088047408560451], dtype=np.int64)   # Note different types here
df2["t"] = np.array([1721088000012322083, 1721088047408560273, 1721088047408560451], dtype=np.uint64)  # Note different types here
# df1["t"] = np.array([32765,32766, 32767], dtype=np.int16)   # Note different types here
# df2["t"] = np.array([32765,32766, 32767], dtype=np.uint16)  # Note different types here
df1["i"] = 1
df2["i"] = 1
df1["p"] = [3, 6, 2]
df2["q"] = [1, 2, 2]

print(pd.merge(df1, df2, on=["i", "t"], how="left", validate="1:1"))
print(pd.merge(df1, df2, on=["t"], how="left", validate="1:1"))
