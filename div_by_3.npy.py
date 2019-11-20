import numpy as np
A=np.arange(1,101).reshape(10,10)
B=A**2
C=B[B%3==0]

