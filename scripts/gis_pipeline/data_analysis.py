import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_sql("SELECT * FROM gis_table", conn)
df.plot(kind="scatter", x="longitude", y="latitude")
plt.show()
