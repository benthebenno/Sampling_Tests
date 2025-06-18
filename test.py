import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm

npArray = np.zeros((5,5))

f, ( (ax7)) = plt.subplots(1, 1, sharex='col', sharey='row')
ax7.imshow(np.real(npArray), cmap=cm.gray)