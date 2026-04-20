import numpy as np

var_coeff=np.array([   
    [4,2],
    [3,5]
])
nbrs=np.array([6,5])

result=np.linalg.solve(var_coeff,nbrs)
print(result)


