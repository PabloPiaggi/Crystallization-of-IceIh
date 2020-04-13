import numpy as np

float_formatter = "{:.3f}".format
np.set_printoptions(formatter={'float_kind':float_formatter})

data=np.genfromtxt("COLVARliquid")
print(np.mean(data,axis=0))

data=np.genfromtxt("COLVARiceih")
print(np.mean(data,axis=0))
