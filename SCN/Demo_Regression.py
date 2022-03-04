from SCN import SCN
import numpy as np
import matplotlib.pyplot as plt
import scipy.io
# Parameter Setting
L_max = 250                    # maximum hidden node number
tol = 0.001                    # training tolerance
T_max = 100                    # maximun candidate nodes number
Lambdas = [0.5, 1, 5, 10, 30, 50, 100, 150, 200, 250]  # scope sequence
r = [0.9, 0.99, 0.999, 0.9999, 0.99999, 0.999999]  # 1-r contraction sequence
nB = 1       # batch size
verbose = 10

# Model Initialization
M = SCN(L_max, T_max, tol, Lambdas, r, nB, verbose)

# load data
mat = scipy.io.loadmat('Demo_Data.mat')
T = mat['T']
X = mat['X']
T2 = mat['T2']
X2 = mat['X2']

per = M.regression(np.array(X), np.array(T))

plt.subplot(3, 1, 1)
plt.plot(range(0, per.shape[1]), per.reshape(-1, 1).tolist(), 'r.-')
plt.axis(ymin=0, ymax=0.20)
plt.legend(['Training RMSE'])

O1 = M.getOutput(X)

plt.subplot(3, 1, 2)
plt.plot(X, T, 'r.-')
plt.plot(X, O1, 'b.-')

plt.legend(['Train Target', 'Model Output'])


O2 = M.getOutput(X2)

plt.subplot(3, 1, 3)
plt.plot(X2, T2, 'r.-')
plt.plot(X2, O2, 'b.-')

plt.legend(['Test Target', 'Model Output'])

plt.show()
