import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

paris_data = pd.read_csv('parisolympics2024.csv')
paris_data.head()
top_10 = paris_data.nsmallest(10, "Position")
plt.xticks(rotation=45, ha='right')
plt.bar(top_10['Country'], top_10['Total Medals'])
plt.show()
