import numpy as np
import matplotlib.pyplot as plt
import pandas


data = pandas.read_csv("houses.csv")

x = data['square_house']
y = data['cost']

x = x[~np.isnan(y)]
y = y[~np.isnan(y)]

def error(f, x, y):
  return np.sum((f(x) - y)**2)
    
f1p, residuals, rank, sv, rcond = np.polyfit(x, y, 1, full=True)
f1 = np.poly1d(f1p)
fx = np.linspace(min(x),max(x),500) 
toPredict = [1650.3, 2200.4]
forecast = f1(toPredict)
#print(forecast)
print(forecast, error(f1, toPredict[0], toPredict[1]))

plt.scatter(x, y, s=10)
plt.plot(fx,f1(fx),linewidth=1.0,color='r')

plt.autoscale(tight=True)
plt.grid(True, linestyle="-", color='0.8')
plt.show()

f1p, residuals, rank, sv, rcond = np.polyfit(x, y, 2, full=True)
f1 = np.poly1d(f1p)
forecast = f1(toPredict)
print(forecast, error(f1, toPredict[0], toPredict[1]))

plt.scatter(x, y, s=10)
plt.plot(fx,f1(fx),linewidth=1.0,color='r')
plt.autoscale(tight=True)
plt.grid(True, linestyle="-", color='0.8')
plt.show()

f1p, residuals, rank, sv, rcond = np.polyfit(x, y, 3, full=True)
f1 = np.poly1d(f1p)
forecast = f1(toPredict)
print(forecast, error(f1, toPredict[0], toPredict[1]))

plt.scatter(x, y, s=10)
plt.plot(fx,f1(fx),linewidth=1.0,color='r')
plt.autoscale(tight=True)
plt.grid(True, linestyle="-", color='0.8')
plt.show()
