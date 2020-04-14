import numpy as np
import matplotlib.pyplot as plt

data=np.genfromtxt("coeffs.data")

numCoeffs=441
numEntries=int(data.shape[0]/numCoeffs)
plt.plot(data[:,2].reshape(numEntries,numCoeffs))

plt.show()
