# Python Tips: Samuel's Approach

> Here you will find a repository of data mining approaches. These approaches will be updated as I found new and improved ways to solve an issue. Please feel free to do a push request if you find a better way of approaching a problem. Thank you for visiting my repository!

## Timing Processes

```
%time 	# time in seconds
%timeit # mean and stdev per loop
```


## Loading and Dumping Data

### Magic Command
```
%matplotlib notebook		# interactive render
%matplotlib inline		# create plot instantly
%matplotlib gtk			# create plot in new window
```

### Imports

```
from scipy.io import loadmat	# for MATLAB files
```

### Data Load

```
mat = loadmat('folder/data.mat')
```

## Dimensionality Reduction

### PCA
> This is for linear relationships.

- Getting Label Colors

```
labels = ['red' if x=='target1' else 'green' for x in df.target]
```

- Dropping Target

```
df.drop('target_name', axis=1, inplace=True)
```

- Removing Nominal Data

```
df1 = df.loc[:, list(df.dtypes!=object)]
```

- Converting Nominal Data to Dummies

```
df2 = pd.get_dummies(df)
```

- Feature Scaling

```
df = df2 # or df1
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df)
df = pd.DataFrame(df_scaled, columns=df.columns)
```

- Applying Principal Component Analysis

```
pca = PCA(n_components=2, svd_solver='auto')
pca.fit(df)
tran = pca.transform(df)
df = pd.DataFrame(tran)
```

- Plotting PCA

```
df.columns = ['comp1', 'comp2']
df.plotscatter(x='comp1', y='comp2', marker='o', c=labels, alpha=0.75)
plt.show()
```

### Isomap
> This is for non-linear relationships.

- Applying Isomap

```
from sklearn.manifold import Isomap
iso = Isomap(n_components=3, n_neighbors=8)
iso.fit(df)
tran = iso.transform(df)
tran =  pd.DataFrame(tran)
tran.columns = ['comp1', 'comp2', 'comp3']
```

- Plotting Isomap 2D

- Using plot

```
tran.plot.scatter(x='comp1', y='comp2', maker='.', alpha=0.7)
plt.title('Plot Version')
plt.show()
```

- Using figure

```
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title('Figure Version')
ax.set_xlabel(tran.comp1.name)
ax.set_ylabel(tran.comp2.name)
ax.scatter(tran.comp1, tran.comp2, maker='.', alpha=0.7)
```

- Plotting Isomap 3D

```
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_title('3D Version')
ax.set_xlabel(tran.comp1.name)
ax.set_ylabel(tran.comp2.name)
ax.set_zlabel(tran.comp3.name)
ax.scatter(tran.comp1, tran.comp2, tran.comp3, color='r', marker='.')
```