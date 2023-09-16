import numpy as np
import pandas as pd
ids=[1,2,3,4,5,6,7]
salaries=[10000,20000,23000,14000,17500,8900,18000]
df=pd.DataFrame({'id':ids,'salary':salaries})



for func in [np.mean,np.sum,np.max,np.argmax,np.min,np.argmin,np.std]:
    print('{} is '.format(func.__name__),end=' ')
    print(func(df['salary']))