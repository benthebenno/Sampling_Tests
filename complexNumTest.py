import matplotlib.pyplot as plt
# from scipy.fft import ifftn 
# from scipy.fft import fftn 
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from roundMatrix import round

f, ((ax1), (ax2), (ax3), (ax7)) = plt.subplots(4, 1, sharex='col', sharey='row')
matrix = np.zeros((5,5))

matrix[1,1] = 1
matrix[1,2] = 1
matrix[2,1] = 1

print("Matrix at the start")
print(matrix)
print("")

print("Fourier")
f_mat = np.fft.fftn(matrix)
print(f_mat)
print("")

print("Reverse")
rev_mat = np.fft.ifftn(f_mat)
print(rev_mat)
print("")

print("Reverse Real")
print(np.real(rev_mat))

newMat = round(rev_mat)
print(newMat)

ax1.imshow(matrix, cmap=cm.gray)
ax2.imshow(np.real(f_mat), cmap=cm.gray)
ax3.imshow(np.real(round(f_mat)), cmap = cm.gray)
ax7.imshow(np.real(newMat), cmap=cm.gray)
plt.show()