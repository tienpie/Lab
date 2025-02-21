import pandas as pd
import numpy as np

# Tạo DataFrame
data = pd.DataFrame({
    "ID": np.arange(1, 1000000,),  
    "Value": np.random.randint(1, 100, 1000000)
})

data["ID"] = data["ID"].astype("int32")
data["Value"] = data["Value"].astype("int8")
data["Value"].value_counts.head(5)
data.query("value >90")
