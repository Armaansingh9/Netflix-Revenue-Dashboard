import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

df = pd.read_excel("Netflix Revenue and Usage Statistics.xlsx",sheet_name='Netflix annual revenue 2011 to ') #load data
#print(df.head()) 
df = df.dropna()

df['Revenue ($bn)'] = df['Revenue ($bn)'].astype(str).str.replace(r'[\$,B]','',regex=True).astype(float)
df['Year'] = df['Year'].astype(int)

df = df.sort_values('Year')

plt.figure(figsize=(10,5))
plt.plot(df['Year'], df['Revenue ($bn)'], marker='o', linestyle='-')
plt.title("Netflix Yearly Revenue (in Billion USD)")
plt.xlabel("Year")
plt.ylabel("Revenue")
plt.grid(True)
plt.tight_layout()
plt.savefig("netflix_yearly_revenue.png")
plt.show()

x = df['Year'].values.reshape(-1,1)
y = df['Revenue ($bn)'].values
model = LinearRegression()
model.fit(x,y)
predicting_years = np.array([[2024],[2025]])
predictions = model.predict(predicting_years)
for year, predictions in zip(predicting_years.flatten(), predictions):
    print(f"Predicted revenue for {year}: ${predictions:.2f}B")

