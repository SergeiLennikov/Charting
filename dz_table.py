import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

data['value'] = 1

one_hot_data = pd.pivot_table(data, values='value', index=data.index, columns='whoAmI', aggfunc='sum').fillna(0)
one_hot_data = one_hot_data.astype(int)
print(one_hot_data)

