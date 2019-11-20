import numpy as np
x=np.random.random((5,5))
xmn=np.mean(x)
xsd=np.std(x)
z=(x-xmn)/xsd

