import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

brackets=["Streamlit","fastapi","devops","MongoDB","AWS"]
# r=range(len(brackets))
count=[120,65,70,100,100]
# avg_marks=[50,55,60,58,40]
# l=[0,1,2,3,4]
# p=[i+.4 for i in r]
# plt.figure(figsize=(5,5))
# plt.bar(brackets,count,width=.4,color='r',edgecolor='k',alpha=.5)
# plt.bar(p,avg_marks,width=.4,color='y',edgecolor='k',alpha=.5)
# plt.xticks([i+.2 for i in l],brackets)
# plt.show()

#Histogram used to check distrubution
# plt.hist(count)

#PIE Chart
plt.pie(count,labels=brackets,autopct=".1f%",explode=(0,1,0,0,0))
plt.show()


