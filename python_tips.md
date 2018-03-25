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

## Data Munging

- **Lowering all Column Names**

```
	df.columns = df.columns.str.lower()
```

- **Coercing Values**

```
	# coercing to numeric
	df.numbers = pd.to_numeric(df.numbers, errors='coerce')

	# coercing to date
	df.date = pd.to_datetime(df.date, errors='coerce')
```

- **Dropping Nulls**

```
	# column drop
	df.dropna(axis=1, inplace=True)

	# row drop
	df.dropna(axis=0, inplace=True)

	# use thresh parameter to specify how many nulls are you willing to keep
```

- **Drop Specific Rows**

```
	# get the row indexes
	drop_this = df[df.col1.isnull()].index

	# drop the stated indexes
	df.drop(drop_this, inplace=True)

	# you migh want to reset index by using df.reset_index
```

- **Drop Specific Columns**

```
	# drop method delete last 2 columns
	df.drop(df.columns[-2:], axis=1, inplace=True)

	# drop method delete specific columns
	df.drop(['colname1', 'colname2'], axis=1, inplace=True)

	# index slicing delete last 2 colums
	df = df.iloc[:, :-2]
```

- **Reset Index***

```
	# shows the old index and new without committing
	df.reset_index()

	# drops the old index and commits
	df.reset_index(drop=True, inplace=True)
```

- **Replace Null Values with Values**

```
	df.fillna(0)
	df.fillna(df.mean(axis=0))
	df.fillna(method='ffill')
	df.fillna(method='bfill')
```

## Exploring Data

- **Null value percentages**

```
	df.isna().sum() / df.count() * 100
```

- **Showing all Rows with Null**

```
	# whole table
	df[df.column_most_null.isnull()]

	# selected columns
	df[['col1', 'col2', 'col3']][df.column_most_null.isnull()]
```

- **Finding Conditions in Rows**

```
	df.col1.str.contains(' ')
```

- **Using Conditions to Find Rows**

```
	# always use parenthesis to avoid errors
	condition = (df.col1.str.contains(' ') & (df.col2.isnull())
	condition = (df.col1 == 'text') | (df.col2 != 'text')
	df[condition]
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

- Importing Images

```
	# Installing imread
	conda config --add channels conda-forge
	conda install imread
```

```
	import scipy
	import os
	import pandas as pd
	from imread import imread

	samples = []
	path = os.getcwd() + '\\folder\\
	files = os.listdir('folder')
	for fname in files:
		file = path + fname
		img = imread(file)
		samples.append((img[::2, ::2]/255.0).reshape(-1))
	df = pd.DataFrame(samples)
```

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

- Plotting Isomap 2D

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
	%matplotlib notebook
	from mpl_toolkits.mplot3d import Axes3D
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	ax.set_title('3D Version')
	ax.set_xlabel(tran.comp1.name)
	ax.set_ylabel(tran.comp2.name)
	ax.set_zlabel(tran.comp3.name)
	ax.scatter(tran.comp1, tran.comp2, tran.comp3, color='r', marker='.')
```

## Classifiers

### K-means

- **Fit the Model**

```
	from sklearn.cluster import KMeans

	# choose the number of clusters
	model = KMeans(n_clusters=4)
	model.fit(df)	
```

- **Plot the Values and Centroids**

```
	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.scatter(df.col1, df.col2, marker='.', alpha=0.3)
	ax.set_title('title')
	ax.set_xlabel('xname')
	ax.set_ylabel('yname')
	centroids = model.cluster_centers_
	ax.scatter(centroids[:,0], centroids[:,1], marker='x', c='r', alpha='0.5, linewidths=3, s=169)
	plt.show()
```