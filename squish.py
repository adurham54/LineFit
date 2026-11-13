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
