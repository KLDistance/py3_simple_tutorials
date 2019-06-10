import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

# data loader
cancer = pd.read_csv('breast_cancer_data.csv')
plt.figure(figsize=(20, 12))
sns.heatmap(cancer.corr(), annot=True)
plt.show()

# so we notice from the heatmap that there is a strong correlation between the 
# mean radius and mean perimeter ; mean area and mean primeter