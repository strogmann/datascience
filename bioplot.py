import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv('cancerdata.csv')
data.head()
plt.scatter(data['creatinine'], data['plasma_CA19_9'])

plt.xlabel("Concentration of Creatinine (mg/dL)")
plt.ylabel("Concentration of Plasma CA19-9 (U/mL)")
plt.show()
