# Ways to concatinate multiple columns
```python
df.iloc[:, 0:3].apply(lambda row: '|'.join(row.values), axis=1)
```
# Ways to look for a list of condition in series
```python
df.series1.isin(['letter', 'number']))
```
# Adjust the legend of a plot
```python
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
```
# Change aestetics of boxplot in matplotlib
https://matplotlib.org/api/_as_gen/matplotlib.pyplot.boxplot.html#matplotlib.pyplot.boxplot
```python
df.series1.plot.box(vert=False, showfliers=True, 
                   flierprops=red_square,
                   showmeans=True,
                   showcaps=True,
                   figsize=(10, 2));
```
