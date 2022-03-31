import numpy as np
from pprint import pprint
#np.savez_compressed('mnist.npz', array1=array1, array2=array2, array3=array3, array4=array4)
b = np.load('mnist.npz')
pprint(b['x_test'])
pprint(b['x_train'])
pprint(b['y_test'])
pprint(b['y_train'])


