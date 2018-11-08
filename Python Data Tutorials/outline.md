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
