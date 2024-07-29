import numpy as np

scores=([12,13,14,15,16])

np.save('binary.npy',scores)

loaded=np.load('binary.npy')
print("original data",scores)
print("loaded data",loaded)
