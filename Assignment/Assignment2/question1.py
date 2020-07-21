import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# load raw material's gene list
path='data.xls'
material_info=pd.read_excel(path,sheet_name='加工原料信息')
info=material_info.iloc[0:16,3:13]

# function to compute kinship
def kinship(x,y):
    lenth=len(x)
    kin=0
    for i in range(0,lenth):
        if x[i]==y[i]:
            kin+=1
    return kin

kin_mat=np.zeros((16,16))
for i in range(0,16):
    for j in range(0,16):
        kin_mat[i][j]=kinship(list(info.iloc[i]),list(info.iloc[j]))

plt.figure()
plt.rcParams['font.sans-serif'] = ['SimHei']
ax = sns.heatmap(kin_mat, cmap='Blues')
plt.xlabel('加工原料品种代码')
plt.ylabel('加工原料品种代码')
plt.savefig('kinship.png')
plt.show()