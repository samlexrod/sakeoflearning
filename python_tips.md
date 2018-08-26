# Python Tips: Samuel's Approach

> Here you will find a repository of data mining approaches. These approaches will be updated as I found new and improved ways to solve an issue. Please feel free to do a push request if you find a better way of approaching a problem. Thank you for visiting my repository!

Data Science Pipeline:

	1. Data Collection
	2. Data Definition
	3. Data Preprocessing
	4. Data Exploration
	5. Predicting Modeling
	6. Reporting


Special Notes about Python:

	1. In python everything is an Object!
	2. Some method calls don't change the object they are called on.
	3. A method is a function inside of a class.


*Get help by adding a ? at the end of the method in question.

# Basics

## Help
```
	# will output information about the function
	help(min)
	?min
```

## IDE
```
	# IDLE is the default
	# VSCode is my preferred
	# PyCharm is not free
	# Spyder is my second favorite
	# Sublimetext is my third favorite
```

## Notebooks
```
	# Jupyter Notebook
	# Azure Notebook
```

## Commenting in Python
```
	#this is a comment
	"""this is 
	a multiline comment"""
	variable = """you can set a multiline 
	comment as a variable"""
```

## String concatenation
> Python concatenates only on string values. Therefore, other data types must be converted to string before concatenation. We can use the string function str() to convert data to string.

```
	# concatenate on print function
	print("You " + "concatenated " + "this " + str(1) + " time.")

	# concatenate on variable
	message_var = "You " + "concatenated " + "this " + str(1) + " time."
```

## Line Continuator Operator
```
	# use backward slash to separate code in lines
	if a == b and c == d and e == f and g == h \
		and i == j and k == l and m == n and o == p \
		and q == r and s == t and u == v and w == x and y == z:
```

## Multi-variable assignment

```
	# color, shape, and texture assignment with list
	color, shape, texture = ['red', 'round', 'soft']

	# color, shape, and texture assignment with values
	color, shape, texture = 'red', 'round', 'soft'

	# swaping variables
	a = 2
	b = 4
	a, b = b, a
```
## Augmented Assignment Operators
```
	# sumation
	spam += 1

	# substraction
	spam -= 1

	# multiplication
	spam *= 1

	# division
	spam /= 1

	# residual
	spam %= 1
```


## None values
> None represents a lack of value. Functions without return statment will return None values.

```
	# the print funciton prints None as default
	print() # Out[1]: 

	# assigning print to a variable assigns None
	spam = print()
	spam == None # Out[1]: True

	# a function withot a return statment will return None
	def this_function():
    	pass

	spam = this_function()
	print(spam == None) Out[1]: True
```

## Global and Local
> Global scope variables can be used everywere. Local scope variables can only be used in the local scope.
> Any local scope variables will be erase from memory after the functions ends.
> Global scope variables will remain in memory until the script is done or the notebook terminated.
> Gobal scope variables can be manipulated at a local level if it is declared as global at the local level.

```
	# this is the global socpe of the variable
	spam = 'global'
	eggs = 'global'

	# this is the local scope of the variable
	def in_function():
		"""any variables here will exist 
		only at the function level"""	
		gobal eggs

		spam = 'local'
		eggs = 'local'

		return spam + ' ' + eggs

	print(in_function()) # Out[1]: local local

	# the local scope does not change the global scope
	print(spam, eggs) # Out[1]: global local
```

## If elif Conditional Steatements
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

	# implicit true or false
	implicit = ''
	if implicit:
		print('implicit must not have blanks to pass')
	else:
		print('implicit have blanks so it pass here')
```

## Built-in Functions

### print()
> The print function will implicitly create a new line.

```
	# print will create a new line
	print('Hello')
	print('World')

	# adding and argument to the parameter end will avoid the new line
	print('Hello', end=' ')
	print('World')

	# the sep paramenter separate items printed in a list
	# by not passing an argument to the sep paramenter, the print
	# statment will concatenate both words withot space as default
	print('Hello', 'World', sep=' ')
```

### type()
```
	type(1)    # prints int
	type("1")  # prints str
	type(1.1)  # prints float
	type(True) # bool
```

### int(), float(), str(), bool()
```
	# these are explicit conversion methods
	int("1") 	 # prints an int
	float("1.1") # prints a float
	bool(1) 	 # prints True

```

### Sorted()
```
	# Sort a list in descending order
	sorted(yourlist, reverse=True)

	# Sorting a dictionary in descending order
	# set itemgetter to 1 to order by value, 0 to order by key
	sorted(yourdict.items(), key=operator.itemgetter(1), reverse=True)
```

### startswith()
```
	str = 'Samuel starts with Sa'
	print(str.startswith('Sa')) #Out[1]: True
	print(str.startswith('Sa', 2, 4)) #Out[1]: False
	print(str.startswith('Sa', -2, len(str))) #Out[1]: True
```

### range()
```
	# create a list from 0 to 3
	range(4)

	# create a list from 1 to 4
	range(1, 5)

	# create a list of the size of a list
	range(len(list))
```

## Custom Functions
```
	# creating the function
	def functionName(parameter1):
		return parameter1

	# calling the funciton
	argument1 = "The console will print this!"
	print(functionName(argument1))
```



## Useful Python Packages and Modules

### random

#### randint()
```
	# import 
	from random import randint

	# get a random numbers from 1 to 20
	rand_num = randint(1, 20) 
```

## Python General Methods

### .format()
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

### .index()
```
	# Finding index in list
	list = [1, 2, 'three', 2]
	list.index('three') # returns 2

	# Finding index in string
	name = 'samuel'
	name.index('s') # returns 0
```

### .count()
```
	# Counting items
	list = [1, 2, 'three', 2]
	list.count(2) # returns 2
```

### .upper(), .lower(), .capitalize()
```
	# Convert a word to all caps
	name = 'samuel'
	name.upper() # returns SAMUEL

	# convert a word to all lower
	name = 'SAMUEL'
	name.lower() # returns samuel

	# Capitalize a word
	name = 'samuel'
	name.capitalize() # returns Samuel
```

### .replace()
```
	# Replace characters or words on strings
	name = 'samuel'
	name.replace('s', 'm') # returns manuel
```

### .append() = x = not needed
```
	# adding to the end of a list
	list = [1, 2, 'three', 2]
	list.append(2) # returns [1, 2, 'three', 2, 2]
```

### .reverse() = x = not needed
```
	# sort values in decending order
	list = [3, 2, 1]
	list.reverse()
```

### .split()
```
	# split a string into a list
	string = 'sammy is awesome!'
	list = string.split(' ')
```

### .strftime()

```
	# example
	from datetime import datetime
	time_now = datetime.now().strftime('%Y-%m-%d')


Directive:

	%a - abbreviated weekday name

	%A - full weekday name

	%b - abbreviated month name

	%B - full month name

	%c - preferred date and time representation

	%C - century number (the year divided by 100, range 00 to 99)

	%d - day of the month (01 to 31)

	%D - same as %m/%d/%y

	%e - day of the month (1 to 31)

	%g - like %G, but without the century

	%G - 4-digit year corresponding to the ISO week number (see %V).

	%h - same as %b

	%H - hour, using a 24-hour clock (00 to 23)

	%I - hour, using a 12-hour clock (01 to 12)

	%j - day of the year (001 to 366)

	%m - month (01 to 12)

	%M - minute

	%n - newline character

	%p - either am or pm according to the given time value

	%r - time in a.m. and p.m. notation

	%R - time in 24 hour notation

	%S - second

	%t - tab character

	%T - current time, equal to %H:%M:%S

	%u - weekday as a number (1 to 7), Monday=1. Warning: In Sun Solaris Sunday=1

	%U - week number of the current year, starting with the first Sunday as the first day of the first week

	%V - The ISO 8601 week number of the current year (01 to 53), where week 1 is the first week that has at least 4 days in the current year, and with Monday as the first day of the week

	%W - week number of the current year, starting with the first Monday as the first day of the first week

	%w - day of the week as a decimal, Sunday=0

	%x - preferred date representation without the time

	%X - preferred time representation without the date

	%y - year without a century (range 00 to 99)

	%Y - year including the century

	%Z or %z - time zone or name or abbreviation

	%% - a literal % character

```

## Lists
> A list is a value that contains values or other lists. Values are called items, which are comma delimited. 

### Declaring, Indexing, Slicing
```
	# declaring list
	listName = []

	# updating list
	listName[0] = "item1"

	# delete from list
	del(listName[0])

	# list with different types
	x = 10
	listDiffTypes = ["1", 2, 3.0, False, x]

	# slicing python lists
	listDiffTypes[start:end]	
	listDiffTypes[0:2] 
	"""the slicing above 
	will print index 0 and 1"""

	# lists of list
	listOfList = [["item1", 23.39], ["item2", 32.39]]

	# indexing matrix
	matrix = [[1, 2], [3, 4]]
	matrix[-1][0] # <- gets 3

	# changing list elements
	list = ['one', 1, 'two', 2]
	list[0:2] = ['three', 3]

	# adding to list
	list = ['one', 1, 'two', 2]
	list = list + ['three', 3]

	# referencing to same location in memory
	x = [1, 2]
	y = x
	y[0] = 2

	"""x at index 0 now will be
	2 since now y and x are referencing 
	to the same location in memory 
	and the reference is the same""" 

	# explicitly changing list
	x = [1, 2]
	y = list(x) # option 1
	y = x[:]    # option 2

	"""y now points to a differet location
	in memory and therefore a change will
	not affect x"""

	# sorting list on decending order
	sorted_list = sorted(list, reverse=True)
```

### Multi-variable assignment with lists
```
	# color, shape, and texture assignment
	color, shape, texture = ['red', 'round', 'soft']
```

### Line Orientation
> There is no need for line continuator when using lists. Python already intepret the list as one line when it is broken in separate lines.
```
	spam = ['one',
			'two',
			'three',
			'four',
			'five']
```

### List Concatenation
> Unlike string concatenation, list concatenation can have multiple data types. Unlike in Numpy (as you will see next), using the plus operator on lists will combine them. 

```
	# concatenate 2 different lists
	list1 = [1, 2, 3]
	list2 = ['four', 'five', 'six']

	list_concat = list1 + list2
```

### in and not in Operator in List
> This operator will return true if a value is found in a list.
```
	# find "two" in the list
	list = [1, 2, 'two', 'three']

	'two' in list #Out[1]: True

	'two' not in list #Out[1]: False
```

### List Statements

#### del
> It is used to delete items from a list by index. It will not leave gaps on the list. Thus, it will shift the index down unles the item deleted is the last item.

```
	# deletion from list
	list = [1, 2, 3]
	del list[1]
```

### List Methods

#### .index()
> Used to find the index of an item. If there are duplicates, the index method will only return the first index.
```

```

#### .insert()
> Inserts an item anywhere inside the list. Assignment to variable is not needed. It is assigned inplace.
```
	# inserting to list
	listName.insert(0, "item2")
```

#### .append() 
> Inserts an item at the end of the list. Assignment to variable is not needed. It is assigned inplace.
```
	# add values to a list
	list = [1, 2]
	list.append(3)
```

#### .remove()
> Removes items from the list, one at a time. It allowes you to specify a value for the deletion, unlike when using the delete statement. Likewise, it will delete only the first item matching the value if there are duplicates. Assignment to variable is not needed. It is assigned inplace.
```
	list = [1, 2, 3]
	
	# remove 3 from the list
	list.remove(3)

```
#### .sort()
> It sort all items in the list on a ascending order by default or a decending order when the reverse parameter is passed as true. If it is applied to strings, it will sort in ASCII-betical order. To sort in true alphabetical order pass the key parameter as str.lower().
```
	# using numbers
	list = [3, 2, 1]

	list.sort() #Out[1]: [1, 2, 3]

	list.sort(reverse=True) #Out[1]: [3, 2, 1]

	# using strings
	list = ['a', 'b', 'C', 'D']

	# sorting on ASCII
	list.sort() #Out[1]: ['C', 'D', 'a', 'b']

	# sorting alphabetically
	list.sort(key=str.lower()) #Out[1]: ['a', 'b', 'C', 'D']
```

### Mutable and Inmutable difference between Str and List
> Strings can act as lists at an individal character level. You can use any method used in list in a string given that it is not attempting to add or remove characters. String values are inmutable unlike list items. But we can use slicing and concatenation to manipulate strings.

#### Manipulating strings
```
	# implicit
	name_msg = 'My name is Danny'
	new_name_msg =  name_msg[:11] + 'Sammy'

	# explicit
	name_msg = 'My name is Danny'
	new_name_msg =  name_msg[:name_msg.index('Da')] + 'Sammy'
```


## Dictionaries
```
	# declaring dictionary
	dicName = {}

	# inserting to dictionary

	# updating dictionary
	dictName["keyname"] = "newkeyname"

	# accessing key values
	dicName["keyname"]
```

## Classes
```
	# declaring a class
	class className:
		
		# creating class properties
		propName = "prop created"

		# set instance variables
		def __init__(self, var1="", var2=""):
			self.var1 = var1
			self.var2 = var2

		# declaring methods
		def methodName(self, parameter1):
			print("print method" + str(parameter1))

	# assigning an object
	callClass = className()

	# calling the methods
	callClass.MethodName()

	# other way to create class properties
	callClass.propName = "prop created"

	# update class property
	callClass.propName = "new prop name"
```

## Loops

### For Loop
```
	# print all items
	for item in listName:
		print(item)

	# print all items by index
	from i in range(1, len(listName)):
		print(listName[i])

	# print ranges from 0 to 9
	from i in range(0, 10):
		print(i)
```

### While Loop
```
	condition = 0
	while condition < 18:
		print(condition)
		condition += 1
```

## Useful Packages

### pyperclip
```
	# copy to clipboard
	pyperclip.copy('text')

	# paste from clipboard
	pyperclip.paste()
```

### Break
```
	while True: #< always true
		print('Hello World!')
		break_word == 'break word'
		if break_word == 'break word':
			break #< breaks the loop
```
### Continue
```
	spam = 0
	while spam < 5:
		spam = spam + 1
		if spam == 3:
			continue
		print('This will be skipped when spam == 3. Look: ' + str(spam))
```

**END BASICS**
---
---

# Intermediate

## Numpy
> Python does not know how to do calculations on list. With Numpy, you can do calculations on lists, which are arrays in Numpy, since you can calculate over entire arrays.
```
	# importing numpy standard
	import numpy as np
```

### Generate Data
```
	# generate 5000 samples

	sample_size = 5000
	mean = np_array.mean()
	std = np_array.std()

	np.random.normal(mean, std, sample_size)
```

### Methods

#### Stacking arrays into columns
```
	# stacking two arrays
	np.column_stack(np_array1, np_array2)

	# both arrays must be of the same size
```

#### Central Tendency and Variability

##### .mean(), .median(), .mode(), .std()
```
	# mean of column one
	np_array = np.array([1, 2, 3], [10, 20, 30])

	# uses 1 and 10, which are in the same column
	In [1]: np.mean(np_array[:, 0])
	Out[1]: 5.5

	# follow the same concept for the other methods
```

#### Measures of Relliability

#### .logical_and()
```
	np.logical_and(df.menage > 30, df.mensalary > 50000)
```

##### .corrcoef()
```
	# correlation between two variables (columns)
	np.corrcoef(np_array[:, 0], np_array[:, 1])
```

### Arrays
> Numpy arrays can only contain one type of data in contrary to a python list. If there is a mix of data types being converted to Numpy array, all values will be converted to string. Boolean values will be converted to the respective boolean integers, 0 or 1. Unlike a list where + adds to the list, a numpy array will do an addition of the arrays. Given that a Numpy array holds only one datatype, it can calculate way faster than going over a python list.

#### Numpy Array Methods

##### .shape
```
	# returns the structure of the array in tuple
	np_array = np.array([[1, 2, 3], [1, 2, 3]])

	In [1]: np_array.shape
	Out[1]: (2, 5)
```

#### Data types rules
```
	# implicit conversion to string
	list = [1, 'one']

	## this returns a numpy array of strings (['1', 'one'], dtype='<U32')
	impl_conversion = np.array(list)

	# implict conversion of boolean
	list = [1, True]

	## this returns a numpy array of integers ([1, 1])
	impl_conversion = np.array(list)
```

#### Calculations
```
	# lists
	list1 = [1, 2, 3]
	list2 = [10, 20, 30]

	# creating numpy arrays
	np_list1 = np.array(list1)
	np_list2 = np.array(list2)

	# this returns a numpy array ([10, 40, 90])
	np_multiplication = np_list1 * np_list2

	# this returns a numpy array ([11, 22, 33])
	np_addition = np_list1 + np_list2

	# this returns a numpy array ([2, 4, 6])
	np_multiplcation = np_list1 * 2
```

#### Boolean array
```
	# np list
	np_list = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

	# values greater than argumet
	greater_than_five = np_list > 5

	# subseting only values that meet condition
	np_list[greater_than_five]
```

#### 2d Arrays
```
	# the idea
	np_array[rows][columns]
	np_array[rows, columns]

	# creating 2d array
	# 1 and 3 are in column1
	# 2 and 4 are in column2
	np_2d_array = np.array([[1, 2], [3, 4]])

	# subsetting 2d array
	In [1]: np_2d_array[0][1]
	Out[1]: 2

	In [2]: np_2d_array[0, 1]
	Out[2]: 2

	In [3]: np_2d_array[0, :]
	Out[3]: array([1, 2])

	# mutiplication by column and array
	In [4]: np_2d_array * np.array([10, 100])
	Out[4]: array([[10, 200], [30, 400]])

```


## The beauty of Pandas
> Unlike general Python and Numpy, pandas can handle different data types in a column or row. The columns correspond to the variables, and the rows correspond to observations.


### Data Load

```
	mat = loadmat('folder/data.mat')

	# if column one has index
	df = pd.read_csv('folder/data.csv', sep=',', index_col=0)
	# if there is no explicit index
	df = pd.read_csv('folder/data.csv', sep=',')

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

### .DataFrame

#### .from_dict()
```
	# convert a dictionary to dataframe
	egdict = {'column1': [1, 2], 'column2': [3, 4]}
	df = pd.DataFrame.from_dict(egdict)

	# pivot column to rows and rename pivoted columns
	egdict = {'column1': [1, 2], 'column2': [3, 4]}
	df = pd.DataFrame.from_dict(egdict, orient='index',
									columns=['rowtocol1', 'rowtocol2'])
```

### Add Columns
```
	# Using a list
	df['column3'] = [True, False]

	# Using extisting columns
	df['column4'] = (df['column1'] + df['column2']) * 10
```

### Rows as Columns
```
	# Access row at index 0 as columns
	egdict.loc[0]
```

### Extract Series or DataFrame
```
	# Extract DataFrame wit double brackets
	df[['column1']]

	## Extract two set of observation from two variables as DataFrame
	df[['column1', 'column2']]

	# Extract Series with single brackets
	df['columnn']
```

### Select an entire row by its row label
```
	df.loc['row_label', :]
```

### Show Non-Objects
```
	# using the .loc[rows, columns] method
	df.loc[:, df.dtypes != object]

	# using the .describe() argument method
	df.describe(exclude=['object'])
```

### Absolute Values
```
	df['number_pos'] = df['number_pos_neg'].abs()
```

### Top N Smallest
```
	N = 5
	df.nsmallest(N, 'number_pos')
```

### Grouping By
```
	# group by and show count only on a selected variable
	df.groupby(['category']).select_variable.count()

	# selecte list of variables
	df.groupby(['category'])['var1', 'var2'].count()

	# group by and show count on all
	df.groupby(['category']).count()

	# Show average by using .mean()
	# Show other descriptive stats
```

### Get the Size of Dataset
```
	# quite simple
	df.size
```

### Drop NaN
```
	# axis=1 is used to drop columns
	# axis=0 is used to drop rows
	# use inplace=True to commit changes

	df.dropna(axis=1, inplace=True)
```

### Convert to Numeric
```
	# Convert object column to numeric
	df['mean'] = pd.to_numeric(df['mean'])
```

## Try Error
```
	# Error handling a zero division

	try:
		return 42/0
	except ZeroDivisionError:
		print('Error: Division by Zero')
```


## Matplotlib

### Basic Plot
```
	# import
	import matplotlib.pyplot as plt

	# example data
	year = [1990, 1991, 1992]
	values = [10, 20, 30]

	# create the plot
	# plt.plot(horizontal_axis, vertical_axis)

	plt.plot(year, values)

	# display the plot
	plt.show()
```

### Basic Fill Between (Area Plot)
```
	# import
	import matplotlib.pyplot as plt

	# example data
	year = [1990, 1991, 1992]
	values = [10, 20, 30]

	# improve the plot
	plt.fill_between(year, values, 0, color='green')

	# name axis and title
	plt.xlabel('horizontal name')
	plt.ylabel('vertical name')
	plt.title('title of chart')
	
	# adjust ticks in billions for example
	plt.yticks([0, 2, 4],
				['0', '2B', '4B'])

	# display the plot
	plt.show()
```

### Basic Multi-Variable Scatter (Bubble)
```
	# import
	import matplotlib.pyplot as plt
	import numpy as np

	# example data
	year = [1990, 1991, 1992]
	values = [10, 20, 30]
	sizes = [100, 20, 300]
	np_sizes = np.array(sizes)

	# create the scatter
	# plt.scatter(horizontal, vertical, s = size, c = color, alpha = transparency)
	plt.scatter(year, values, s = np_sizes)

	# name axis and title
	plt.xlabel('horizontal name')
	plt.ylabel('vertical name')
	plt.title('title of chart')
	
	# adjust ticks in billions for example
	plt.yticks([0, 2, 4],
				['0', '2B', '4B'])

	# display the scatter plot
	plt.show()
```

### Adding Text and Grids
```
	plt.text(h_location, v_location, 'text')
	plt.grid(True)
```

### Handling Ticks
```
	import numpy as np
	# list of positions at which ticks should be placed
	locs = np.arange(len(variable.index))

	# explicit labels to place at given locs
	## variable must be a DataFrame
	labels = variable.index

	# the rotation argument is the alignment
	r = 'vertical'

	# set ticks
	plt.xticks(
		locs,
		labels,
		rotation = r
	)

```


### Scatter Parameters
```
	# called using plt.scatter()
	# also called using df.plot(kind='scatter')
	# color or c = color of points
	# marker = type of point
```

### Histogram Parameters
```
	# called using plt.hist()
	# also called using df.plot(kind='hist')
	# bins = grouping of values, or brackets
```

### Plot Parameters
```
	# called using plt.plot()
	# create bar by using kind='bar'
```

## Grammar of Graphics (ggplot) in Python

**END INTERMEDIATE**
---
---

# Advanced

## Version Check
```
	import numpy
	numpy.version.version
	numpy.__version__
```
## Timing Processes

```
	%time 	# time in seconds
	%timeit # mean and stdev per loop
```

## Magic Command
```
	%matplotlib notebook				# interactive render
	%matplotlib inline				# create plot instantly
	%matplotlib gtk					# create plot in new window
	matplotlibe.style.use('ggplot') # ggplot look
```

## Imports

```
	from scipy.io import loadmat			# for MATLAB files
	from scipy import misc 					# for images
	from scipy.io.wavfile import wavfile 	# for audio
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

### **Show Only Columns with Object Values**

> This is useful to investigate why values did not automatically converted to numeric.

```
	df.loc[:, df.dtypes==object]
```

### **Comparing Variances**

```
	(df.std()*2).sort_values(ascending=False)
```

### **Getting a Random Sample of Dataset**

```
	# set the sampling random seed
	np.random.seed(0)

	# get your sample of x rows
	df.sample(x)
```

### **Subsetting Dataset**

```
	# slicing by column name
	df.loc[:, ['col1', 'col2']]
	df.loc[:, 'col1':'col10']

	# slicing by index
	df.iloc[:, [0, 1]]
	df.iloc[:, 0:9]
```

### **Null Value Percentages**

```
	# get the values per features
	df.isna().sum() / df.shape[0] * 100

	# get the values in overall
	df.isna().sum().sum() / np.product(df.shape)	
```

### **Showing all Rows with Null**

```
	# whole table
	df[df.column_most_null.isnull()]

	# selected columns
	df[['col1', 'col2', 'col3']][df.column_most_null.isnull()]
```

### **Finding Conditions in Rows**

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

### **Using Conditions to Find Rows**

```
	# always use parenthesis to avoid errors
	condition = (df.col1.str.contains(' ') & (df.col2.isnull())
	condition = (df.col1 == 'text') | (df.col2 != 'text')
	df_new = df.loc[condition]
```

### **Grouping Aggregates**

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

### **Unique Values**

```
	# listing unique values
	df.col1.unique()

	# counting unique values
	df.col1.value_counts()	

	# counting count of unique values
	df.col1.value_counts().count()
```

### **Investigating Data Types**

```
	df.dtypes
```

### **Descriptive Statistics**

```
	df.describe()
```

### **Wildcard**

```
	df[df.col1.str.find('str') >= 0]
```

### **Quick Problems**
> 1. Using numpy, find the year where the company turned
profits higher than $100 millions

```
	# data in list
	profit_in_mil = [90, 100, 120, 200]
	years = [2000, 2001, 2002, 2003]

	# converting to numpy
	np_profit = np.array(profit_in_mil)
	np_years = np.array(years)

	# conditional subsetting profit
	condition = np_profit > 100

	# finding the minimun year
	np_year[condition].min()

	Out[1]: 2002
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

## Python Pain Killers

### References of lists in memory
```
	# the pain
	def bacon(bake_beans):
		bake_beans.append("I don't like Spam")
	
	spam = [1, 2, 3]
	bacon(spam)
	print(spam)

	#Out[1]: [1, 2, 3, 'I don't like Spam']

	# the pain killer
	def bacon(bake_beans):
		bake_beans.append("I don't like Spam")
	
	spam = [1, 2, 3]
	bacon(spam[:]) #<- index to create another reference
	print(spam)

	#Out[1]: [1, 2, 3, 'I don't like Spam']
```

# Other

## django
```
	# installing django using Anaconda Distribution
	# type the desired version after the double equal signs
	conda install django==2.0.2

	# creating project
	django-admin startproject projectname

	# add application to project
	python manage.py startapp appname

	# creating migration
	python manage.py makemigrations

	# migrate a database
	python manage.py migrate

	# create superuser
	python manage.py createsuperuser

	# collecting static files into one folder
	python manage.py collectstatic

	# deploying django
	python manage.py runserver
```
### dango Pain Killers
```
	# Always start your classes with capital letters
	class Product(request):

	"""
	This will avoid issues between variables and classes.
	"""
```

### {% csrf_token %}
> Use it whenever there is a POST request to prevent csrf attacks.

### .gitignore
```
	# get the default gitignore files
	1. Go to gitignore.io
	2. In the search bar, type django
	3. Copy the code

	# ignore sensitive commits
	1. Create a new file and name it .gitignore
	2. In the file, paste the code found in gitignore.io
```

### writing code in HTML

#### create views
```
	# these are the request to the pages
	# you can write your code here
	# create functions
	def home(request)
		return render(request, 'home.html')
	
	def target_here1(request):
		pass # write code here

	def target_here2(request):
		pass # write code here
```

#### create the urlpatterns
```
	# from . import views

	# for the links to work you must create paths
	urlpatterns = [
		path('', views.home, name='home'),
		path('count/', views.count, name='target_here1'),
		path('about/', views.about, name='target_here2')
	]
```

#### a tag references to pages
```
	# Send to target on a hyperlink
	<a href='{% url 'target_here' %}'></a>
```

#### getting references
```
	# in the html script
	# example of an html form
	<form action="{% url 'target_here2' %}">
		<textarea cols="40" rows="5" name="fulltext"></textarea>
		<br/>
		<input type="submit" value="Count!"/>
	</form>

	# inside the views.py
	# assigning the fulltext into variable
	fulltext = request.GET['fulltext']

	# write your python code in the view
```

#### for loop
```
	# for loop on list
	{% for item in list %}
	{{ item }}
	{% endfor %}

	# for loop on dictionary
	{% for key, value in thisdict %}
	{{ key }}
	<br/>
	{{ value }}
	<br/>
	<% endfor %>

```

#### now function
```
	# If the date is Sautrday, August 8, 2018

	#Y = 2018
	#y = 18
	#M = Aug
	#m = 08
	#D = Sat
	#d = 11

	{% now "Y" %}
```

#### Setting up Models & Migrations

### Starting A Project Basic Step by Step

#### 1. Create a project
```
	# in anaconda distribution command line
	>python manage.py startproject projectname

	# in anaconda distribution command line
	>rename projectname projectname-project
```

#### 2. Connect to database
```
	# in settings.py
	DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'projectname',
        'USER': 'postgres',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
#### 3. Migrate to database
```
	# in anaconda distribution comman line
	>python manage.py migrate
```

#### 4. Create apps
```
	# in anaconda distribution command line
	>python manage.py startapp appname
```

#### 5. Create home and other funcitons in the views
```
	# in the veiws.py
	def home(request):
		return render(request, 'appname/home.html')
```

#### 6. Make new folder(s) and file(s) template/appname/*.html file(s) folder under the appname

#### 7. Create path for apps
```
	# import the views from the app
	from appname.views.views import home

	# create the path for home
	path('', home, name='home')
```

#### 8. Add app to settings
```
	# in settings.py
	INSTALLED_APPS = [
	'appname.apps.AppnameConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',]
```

#### 9. Create a projectname/templates/base.html file
```
	# add the base.html folder to the directory
	TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['projectname/templates'], #<-- This is the folder to add, the rest is defaulted
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

	# the key is in the middle to where other *.html files will fill conent
	Top content

	{% block content %}
	{% endblock %}

	Bottom content

	# in *.html
	{% extends 'base.html' %}
	{% block content %}
	Any content here...
	{% endblock %}
```

#### 10. Add static folders and set the static root
```
	# create a appname/static folder to insert any images or static files

	# in the *.html page under the head tag
	{% load staticfiles %}

	# go to settings.py and create the static root
	STATIC_ROOT = os.path.join(BASE_DIR, 'static')
	STATIC_URL = '/static/'

	# create a link to static files outside of apps
	STATICFILES_DIR = [
		os.path.join(BASE_DIR, 'projectname/static/')
	]

	# in the anaconda prompt collect static
	>python manage.py collectstatic
```



## Anaconda Prompt

### Enviroments
https://conda.io/docs/user-guide/tasks/manage-environments.html

```
	# create environment
	conda create --name myenv

	# activate environment
	conda activate myenv

	# deactivate environment
	deactivate

	# see the list on environments
	conda env list

	# removing environment
	conda remove --name myenv --all

	# get requirements
	conda freeze > requirements.txt

	# installing from other environment
	conda install -r requirements.txt
```
