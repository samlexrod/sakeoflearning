# Python Tips: Samuel's Approach

> Here you will find a repository of data mining approaches. These approaches will be updated as I found new and improved ways to solve an issue. Please feel free to do a push request if you find a better way of approaching a problem. Thank you for visiting my repository!


## Loading and Dumping Data

### Magic Command
```
%matplotlib notebook	# interactive render
%matplotlib inline		# create plot instantly
%matplotlib gtk			# create plot in new window
```

## Dimensionality Reduction

### PCA

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
