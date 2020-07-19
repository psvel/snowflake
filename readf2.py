import pandas as pd 
import numpy as np
import sys
data = pd.read_csv(sys.argv[1])
# Preview the first 5 lines of the loaded data 
data.head()
print(data.to_numpy)
print(data.values.tolist())
print(np.asarray(data.values.tolist()))
