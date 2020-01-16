# import scipy as sp
# from matplotlib import pyplot as plt
# import numpy as np
# from collections import Counter
from matplotlib import pyplot as plt
import numpy as np

x = np.linspace(0.1, 2 * np.pi, 41)
y = np.exp(np.sin(x))
plt.stem(x, y, use_line_collection = True)
plt.show()