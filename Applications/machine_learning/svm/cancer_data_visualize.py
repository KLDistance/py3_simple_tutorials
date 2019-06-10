import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

# data loader
cancer = pd.read_csv('breast_cancer_data.csv')

# data visualize
visual_column_list = ['radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean', 'smoothness_mean']
sns.pairplot(cancer, vars=visual_column_list)
plt.show()

# show targets, where B (orange) is benign and M (blue) is malignant
sns.pairplot(cancer, hue='diagnosis', vars=visual_column_list)
plt.show()