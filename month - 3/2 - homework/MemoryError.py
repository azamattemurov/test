try:
 import numpy as np
 np.random.uniform(low=1,high=10,size=(10000,100000))
except:
 print('Bu esa MemoryError')

 # Errorni ko'rmoqchi bolsangiz try va exceptni o'chiring !