import pandas as pd
import numpy as np

data = {
"ID" : [101,102,103,104,105],
"Name" : ["Quynh Nhu", "Hoang Hai", None, "Phuong Tuan","Thien An"],
"Age":[26,18,20,None,19],
"Salary" : [50000,35000,65000,100000,None]
}
df = pd.DataFrame(data)
age_mean = df["Age"].mean()
df["Age"].fillna(age_mean, inplace=True)

# đien gia tri thieu trong coi Age = gia tri trung binh
df.dropna(inplace=True)
df["Name"].fillna("Unknown",inplace=True)
df["Salary"].interpolate(methode="linear",inplace=True)
print(df)
