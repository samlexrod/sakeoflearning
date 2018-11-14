# Ideas to cover
- pandas index
  - transpose pd.DataFrame({'col1': [1, 2, 3, 4, 5]
  - reset_index
  - rename columns
  example:
  
```python
df = pd.DataFrame({'col1': ['map1'], 'col2': ['map2'], 'col3': ['map3']})
df= df.T.reset_index()
df.columns = ['column', 'map']
df
```

```python
df = pd.DataFrame({'col1': ['map1'], 'col2': ['map2'], 'col3': ['map3']})
df= df.T.reset_index()
df.columns = ['column', 'map']
df.set_index('column', inplace=True)
df.to_dict('records')
```

-Assign only where condition meet with multiple conditions
```python
import pandas as pd
import numpy as np

df = pd.DataFrame({'col1': ['a', 'b', 'c', 6, 7, 8, '?'], 'col2': ['letter', 'letter', 'letter', 'number', 'number', 'number', 'question']})
conditions = (df.col2.isin(['letter', 'number']))
print(conditions)
df['col3'] = np.where(conditions, df.col2 + ' ' + df.col1.astype(str), df.col1)
display(df)
```

-Melt tutorial
```python

```
