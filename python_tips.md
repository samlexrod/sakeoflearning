# Python Tips: Samuel's Approach

> Here you will find a repository of data mining approaches. These approaches will be updated as I found new and improved ways to solve an issue. Please feel free to do a push request if you find a better way of approaching a problem. Thank you for visiting my repository!

Data Science Pipeline

	1. Data Collection
	2. Data Definition
	3. Data Preprocessing
	4. Data Exploration
	5. Predicting Modeling
	6. Reporting


*Get help by adding a ? at the end of the method in question.

# Basics

## Commenting in Python
```
	#this is a comment
	"""this is 
	a multiline comment"""
	variable = """you can set a multiline 
	comment as a variable"""
```

## Conditional Steatements
```
	"""
	== equals
	> greater than
	>= greater than or equal to
	< less than
	<= less than or equal to
	<> not equal
	!= not equal
	"""

	# this is a conditional statement
	if 1 = 1:
		print("One indeed equal to one")
	elif 1 = 2:
		print("One does not equal to two, but will not run because the first one will")
	else:
		print("Will not run on this condition")
```


## Functions
```
	# creating the function
	def functionName(parameter1):
		return parameter1

	# calling the funciton
	print(functionName("The console will print this!"))
```

## Methods

### Using the format object
```
	# basic formatting

	print("Hello {}, your balance is {}.".format("Brian", 30.30))
	print("Hello {0}, your balance is {1}.".format("Brian", 30.30))
	print("Hello {1}, your balance is {0}.".format(30.30, "Brian"))
	print("Hello {name}, your balance is {amt}.".format(name = "Brian", amt = 30.30))
	print("Hello {0}, your balance is {amt}.".format("Brian", amt = 30.30))

	# number formatting

	"""
	d	Decimal integer
	c	Corresponding Unicode character
	b	Binary format
	o	Octal format
	x	Hexadecimal format (lower case)
	X	Hexadecimal format (upper case)
	n	Same as 'd'. Except it uses current locale setting for number separator
	e	Exponential notation. (lowercase e)
	E	Exponential notation (uppercase E)
	f	Displays fixed point number (Default: 6)
	F	Same as 'f'. Except displays 'inf' as 'INF' and 'nan' as 'NAN'
	g	General format. Rounds number to p significant digits. (Default precision: 6)
	G	Same as 'g'. Except switches to 'E' if the number is large.
	%	Percentage. Multiples by 100 and puts % at the end.
	"""

	# it shows 123
	print("The integer is {:d}".format(123))

	# it shows 123.67
	print("The float number is {:f}".format(123.67))

	# it shows 12%
	print("The percentage is {:%}".format(.12))
```

END BASIC***

# Advanced

## Timing Processes

```
	%time 	# time in seconds
	%timeit # mean and stdev per loop
```

## Loading and Dumping Data

### Magic Command
```
	%matplotlib notebook				# interactive render
	%matplotlib inline				# create plot instantly
	%matplotlib gtk					# create plot in new window
	matplotlibe.style.use('ggplot') # ggplot look
```

### Imports

```
	from scipy.io import loadmat			# for MATLAB files
	from scipy import misc 					# for images
	from scipy.io.wavfile import wavfile 	# for audio
```

### Data Load

```
	mat = loadmat('folder/data.mat')
	df = pd.read_csv('folder/data.csv', sep=',', index_col=0)
	df = pd.read_sql_table('tablename', engine, columns=['col1', 'col2'])
	df = pd.read_excel('folder/data.xlsx', 'Sheet1', na_values=['NA', '?'])
	df = pd.read_json('folder/data.json', orient='columns')
	df = pd.read_html('http://page.com/with/table.html')[0]
	img = misc.imread('image.png')
	sample_rate, audio_data = wavefile.read('sound.wav')
```

### Data Dump

```
	df.to_sql('table', engine)
	df.to_excel('folder/data.xlsx')
	df.to_jason('folder/data.json')
	df.to_csv('folder/data.csf')
```

## Data Munging

- **Altering Column Names**

```
	# lowering column names
	df.columns = df.columns.str.lower()

	# changing column names
	df.columns = ['col1', 'col2', 'col3']

	# replacing characters using lambda
	df.columns = pd.Series(df.columns).apply(lamba x: x.replace('-', '_'))

	# replacing characters using inline function
	df.columns = [x.replace('-', '_') for x in df.columns]
```

- **Coercing Values**

```
	# coercing to numeric
	df.numbers = pd.to_numeric(df.numbers, errors='coerce')

	# coercing to date
	df.date = pd.to_datetime(df.date, errors='coerce')

	# coercing to time
	df.time = pd.to_timedelta(df.time, errors='coerce') 
```

- **Whole Dataframe to Numeric Ignoring Errors**

```
	for header in df.columns:
		df[header] = pd.to_numeric(df[header], errors='ignore')
```

- **Formatting Values**

```
	# specific format
	pd.to_datetime(df.date, format = "%m/%d/%y")

	# inferring format if at least one is different
	pd.to_datetime(df.date, infer_datetime_format=True)
```

- **Dropping Nulls**

```
	# column drop
	df.dropna(axis=1, inplace=True)

	# row drop, which is the default
	df.dropna(axis=0, inplace=True)

	# use thresh parameter to specify how many nulls are you willing to keep
```

- **Drop Specific Rows**

```
	# get the row indexes
	drop_this = df[df.col1.isnull()].index
	drop_this = df[df.col1 == 'this'].index

	# drop the stated indexes, axis=0 is defualt
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

- **Drop Duplicates**

```
	# using all features
	df.drop_duplicates()

	# using only a subset of features
	df.drop_duplicates(subset=['col1', 'col2'])
```

- **Reset Index**

```
	# shows the old index and new without committing
	df.reset_index()

	# drops the old index and commits
	df.reset_index(drop=True, inplace=True)
```

- **Imputations: Replace Null Values with Values**

```
	# fill with zero
	df.fillna(0)

	# fill with the mean of each row
	df.fillna(df.mean(axis=0))

	# fill with values directly above
	df.fillna(method='ffill')

	# fill with values directly below
	df.fillna(method='bfill')

	# fill value limits
	df.fillna(value=0, limit=3)

	# fill interpolating with non-nans
	df.interpolate(method='polynomial', order=2)
```

- **Replacing Non-numeric Values**

```
	import re
	df.col1.apply(lambda x: re.sub('[^0-9]', '', str(x))
```

- **Drop Non-numeric Columns**

```
	df.drop(df.columns[df.dtypes == object], axis=1, inplace=True)
```

## Exploring Data

- **Show Only Columns with Object Values**

> This is useful to investigate why values did not automatically converted to numeric.

```
	df.loc[:, df.dtypes==object]
```

- **Comparing Variances**

```
	(df.std()*2).sort_values(ascending=False)
```

- **Getting a Random Sample of Dataset**

```
	# set the sampling random seed
	np.random.seed(0)

	# get your sample of x rows
	df.sample(x)
```

- **Subsetting Dataset**

```
	# slicing by column name
	df.loc[:, ['col1', 'col2']]
	df.loc[:, 'col1':'col10']

	# slicing by index
	df.iloc[:, [0, 1]]
	df.iloc[:, 0:9]
```

- **Null Value Percentages**

```
	# get the values per features
	df.isna().sum() / df.shape[0] * 100

	# get the values in overall
	df.isna().sum().sum() / np.product(df.shape)	
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
	# conditions on string
	df.col1.str.contains(' ')

	# conditions not on string
	df.col1.astype('str').str.contains('727')

	# multiple conditions
	condition = (df.col1 == 'text') | \
		    ((df.col1 == 0) & \
		    (df.col2 == 30))
```

- **Using Conditions to Find Rows**

```
	# always use parenthesis to avoid errors
	condition = (df.col1.str.contains(' ') & (df.col2.isnull())
	condition = (df.col1 == 'text') | (df.col2 != 'text')
	df_new = df.loc[condition]
```

- **Grouping Aggregates**

```
	# counting the number of values
	df.groupby(['col1']).count()

	# summing the numric values
	df.groupby(['col1']).sum()

	# average by group
	df.groupby(['col1']).mean()	

	# aggregate and select one column
	df.groupby(['col1'])[['col2']].sum()
```

- **Unique Values**

```
	# listing unique values
	df.col1.unique()

	# counting unique values
	df.col1.value_counts()	

	# counting count of unique values
	df.col1.value_counts().count()
```

- **Investigating Data Types**

```
	df.dtypes
```

- **Descriptive Statistics**

```
	df.describe()
```

- **Wildcard**

```
	df[df.col1.str.find('str') >= 0]
```

## Exploring Visually

- **Making Matplotlib look Pretty**

```
	matplotlib.style.use('ggplot')
```

- **Using colormaps**

```
	import matplotlib.pyplot as plt

	plt.cm. # press tab to see selections
```

### Pandas Dataframe Visuals

- **Quick Plots**

```
	df.plot. # press tab to see the list of options

	# wisker plot
	df.plot.box()

	# histogram with transparency and customized bins
	df.col1.plot.hist(alpha=0.4, bins=3)

	# scatterplot
	df.plot.scatter(x='col1', y='col2')
```

### Matplotlib & Tools

- **3d Plots**

```
	import matplotlib.pyplot as plt
	from mpl_toolkits.mplot3d import Axes3D
	%matplotlib notebook

	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	ax.set_xlabel(df.col1.name)
	ax.set_ylabel(df.col2.name)
	ax.set_zlabel(df.col3.name)
	
	ax.scatter(df.col1, df.col2, df.col3, c='r', marker='.')
	plt.show()
```

- **Parallel Coordinates**

```
	import matplotlib.pyplot as plt
	from pandas.tools.plotting import parallel_coordinates
	
	plt.figure()
	parallel_coordinates(df, 'target_names')
	plt.show()	
```

- **Andrew's Curves**

```
	import matplotlib.pyplot as plt
	from pandas.tools.plotting import andrews_curves

	plt.figure()
	andrews_curves(df, 'target_names')
	plt.show()
```

- **IM Show**

```
	import matplotlib.pyplot as plt
	
	plt.imshow(df.cor(), cmap=plt.cm.Blues, interpolation='nearest')
	plt.colorbars()
	tick_marks = [i for i in range(len(df.columns))]
	tick_marks = [i for i, c in enumerate(df.columns)] # use either or
	plt.xticks(tick_marks, df.columns, rotation='vertical')
	plt.yticks(tick_marks, df.columns)

	plt.show()
```

### Seaborn

- **Subplots Using Seaborn**

```
	import seaborn as sns

	# use this to have one graph in 2 grid rows
	fig, ax = plt.subplots(2, 1)

	# use this to have two graphs in one grid row
	fig, ax = plt.subplots(1, 2)

	# rest of the code
	ax[0].set_title('Plot1')
	ax[1].set_title('Plot2')
	sns.distplot(df.col1, ax=ax[0])
	sns.distplot(df.col2, ax=ax[1])	
```

- **Gaussian Density Only w/ Adjusted Bins**

```
	sns.distplot(df.col1, kde=True, hist=False, bins=31
```

## Transforming Data
[http://http://pandas.pydata.org/pandas-docs/stable/merging.html](http://http://pandas.pydata.org/pandas-docs/stable/merging.html "Best to go here!")


- **Removing Outliers** 


- **SQL Union**

```
	df = df.append(df2)
```
## Scaling Methods

- **Sklearn Scalers**

```
	from sklearn import preprocessing as pre

	tran = pre.StandardScaler().fit_transform(df)
	tran = pre.MinMaxScaler().fit_transform(df)
	tran = pre.MaxAbsScaler().fit_transform(df)
	tran = pre.Normalizer().fit_transform(df)
```

- **Mlxtend Scalers**

```
	from mlxtend import preprocessing as pre

	tran = pre.minmax_scaling(df.col1, columns = [0])
```

- **Scaling Images**

```
	# resampling an image
	img = img[::2, ::2]

	# scaling colors to grayscale
	X = (img / 255.0).reshape(-1)

	# scaling colors preserved
	X = (img / 255.0).reshape(-1, 3)

	# looping in folder
	import os
	files = os.listdir('folder_name')
	dset = []
	for fname in files:
		img = misc.imread(fname)
		dset.append((img / 255.0).reshape(-1))
```

## Normalizing Methods

- **Box-Cox Transformation**

```
	from scipy import stats

	norm_data = stats.boxcox(df.col1)[0]
```

## Encoding Methods

- **Character Encoding/Decoding**

```
	# encoding
	x.encode('utf-8', errors = "replace")

	# decoding
	x.decode('utf-8')
```

- **Chardet for Identifying Encoding, not 100% Accurate**

```
	# read file to identify encoding
	with open('folter/file.csv', 'rb') as rawdata:

		# increase read size if results are inaccurate
		result = chardet.detect(rawdata.read(10000))

	# load data with identified encoding
	data = pd.read_csv('folder/file.csv', encoding = result['encoding'])
```

- **Encoding Features**

```
	# creates numbering by alphabetical categories
	# prefered for Nominal features
	df['col1_ec'] = df.col1.astype('category').cat.codes

	# prefered for Ordinal features
	ordered_features = ['ord1', 'ord2', 'ord3']
	df['col1_ec'] = df.col1.astype('category', ordered=True, categories=ordered_features).cat.codes

	# create new features of 1 and 0 encodings
	df = pd.get_dummies(df, columns=['col1'])
```

## Bag of Words

```
	from sklearn.feature_extrction.text import CountVectorizer

	bow = CountVectorizer()
	
	X = bow.fit_transform(textdata)

	bow.get_feature_names()

	X.toarray()
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
	df =  pd.DataFrame(tran)
	df.columns = ['comp1', 'comp2', 'comp3']
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

- **Running KMeans on PCA**


```
	# selecting colors and scaling
	c_color_list = ['r', ''g', 'b', 'o']
	labels = model.labels_
	df_t = preprocessing.MinMaxScaler().fit_transform(df)
	c_color = [c_color_list[label[i]] for i in range(len(df_t))]

	# processing PCA
	pca = PCA(n_components=2, svd_solver='randomized', random_state=7)
	pca.fit(df_t)
	tran = pca.transform(df_t)
	df_t = pd.DataFrame(df_t, columns=['col1', 'col2'])
	
	# plotting
	ax.scatter(df_t.col1, df_t.col2, c=c_color, marker='o', alpha=0.2)	
```
