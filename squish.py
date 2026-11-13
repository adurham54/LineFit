import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.stats import norm
from fitting_functions import *

data = np.loadtxt("project2_data.csv", delimiter=",", dtype = str)

x = data[1:, 0].astype(np.float32)
y = data[1:, 1].astype(np.float32)

params, params_cov = scipy.optimize.curve_fit(linear, x, y)
slope = params[0]
intercept = params[1]

### Exercise 1

print_equation(slope, intercept, "grams", "mm")
# Equation of the line: y= -0.06214285719244612 mm/gram + 63.214285727922686 mm

### Exercise 2
fig = plt.figure()
plt.scatter(x, y, label='Data')
plt.plot(x, linear(x, slope, intercept),label='Linear Fit') 
plt.legend(loc='best')
plt.xlabel("mass(g)") 
plt.ylabel("height(mm)")  
plt.show()
fig.savefig('dataplot.png')
