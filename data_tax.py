import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("tax_spending (1).csv")

spending = {}
counta = 0
while counta < data.shape[0] - 3:     
    key = data['R billion'][counta]
    value = float(data.iloc[counta][2:-2].sum())
    spending[key] = value
    counta += 1
    
sns.set_theme()
plt.barh([i for i in spending.keys()], [m for m in spending.values()])
plt.xlabel("spending in ZAR (Billions)", fontsize = 15 ,fontweight= 'bold', labelpad=20)
plt.ylabel("Functional Classification", fontsize = 15 , fontweight= 'bold' ,labelpad=20)
plt.title("CONSOLIDATED SPENDING BY FUNCTIONAL AND ECONOMIC CLASSIFICATION 2026/2027",fontweight= 'bold', fontsize= 20)
plt.grid(True,linestyle = "--")
plt.show()
    
    
