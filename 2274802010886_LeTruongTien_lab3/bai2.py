import pandas as pd
import numpy as np

df1 = pd.DataFrame({
    "Id": [1, 2, 3],
    "Score_A": [70, 90, 85]
})

df2 = pd.DataFrame({
    "Id": [3, 4, 5],
    "Score_B": [62, 91, 75]
})

inner_join = pd.merge(df1, df2, on="Id", how="inner")
print("Inner Join:")
print(inner_join)
vertical_concat = pd.concat([df1, df2], axis=0, ignore_index=True)
print("\nVertical Concatenation:")
print(vertical_concat)
merged_df = df1.set_index("Id").combine_first(df2.set_index("Id")).reset_index()
print("\nMerged DataFrame:")
print(merged_df)
