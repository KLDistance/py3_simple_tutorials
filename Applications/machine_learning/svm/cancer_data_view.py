import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# data loader
cancer = pd.read_csv('breast_cancer_data.csv')
print(cancer.head())
print()
print(cancer.shape)
print(cancer.columns)

'''
we have to know the meaning of each column:

mean radius = mean of distances from center to points on the perimeter
mean texture = standard deviation of gray-scale values
mean perimeter = mean size of the core tumor
mean area = ...
mean smoothness = mean of local variation in radius lengths
mean compactness = mean of perimeter^2 / area - 1.0
mean concavity = mean of severity of concave portions of the contour
mean concave points = mean for number of concave portions of the contour
mean symmetry = ...
mean fractal dimension = mean for "coastline approximation" - 1
radius error = standard error for the mean of distances from center to points on the perimeter
texture error = standard error for standard deviation of gray-scale values
perimeter error = ...
area error = ...
smoothness error = standard error for local variation in radius lengths
compactness error = standard error for perimeter^2 / area - 1.0
concavity error = standard error for severity of concave portions of the contour
concave points error = standard error for number of concave portions of the contour
symmetry error = ...
fractal dimension error = standard error for "coastline approximation" - 1
worst radius = "worst" or largest mean value for mean of distances from center to points on the perimeter
worst texture = "worst" or largest mean value for standard deviation of gray-scale values
worst perimeter = ...
worst smoothness = "worst" or largest mean value for local variation in radius lengths
worst compactness = "worst" or largest mean value for perimeter^2 / area - 1.0
worst concavity = "worst" or largest mean value for severity of concave portions of the contour
worst concave points = "worst" or largest mean value for number of concave portions of the contour
worst fractal dimension = "worst" or largest mean value for "coastline approximation" - 1
'''