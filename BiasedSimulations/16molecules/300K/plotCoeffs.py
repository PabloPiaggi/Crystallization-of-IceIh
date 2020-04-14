import numpy as np
import matplotlib.pyplot as plt

data=np.genfromtxt("coeffs.data")

numCoeffs=21
numEntries=int(data.shape[0]/numCoeffs)
plt.plot(data[:,1].reshape(numEntries,numCoeffs))

plt.show()
