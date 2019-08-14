# Ways to concatinate multiple columns
```python
df.iloc[:, 0:3].apply(lambda row: '|'.join(row.values), axis=1)
```
# Ways to look for a list of condition in series
```python
df.series1.isin(['letter', 'number']))
```
