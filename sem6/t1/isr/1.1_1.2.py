import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
import pandas

data = pandas.read_csv("houses.csv")

x = data['square_house']
y = data['cost']

# среднее значение
def mean(d):
  s_d = sum(d)
  mean_value = sum(d)/len(d)
  return mean_value

# дисперсия
def dispersion(d):
  d_first = [(i - mean(d)) ** 2 for i in d] 
  res = sum(d_first)/(len(d_first))
  return res

# СКО
def sko(d):
  return sqrt(dispersion(d))

# среднее значение numpy
def mean_np(d):
  return np.mean(d)

# дисперсия numpy
def dispersion_np(d):
  return np.var(d)

# СКО numpy
def sko_np(d):
  return np.std(d)

print(mean(x))
print(mean_np(x))
print(dispersion(x))
print(dispersion_np(x))
print(sko_np(x))
print(sko(x))
