# Translation Test Dataset

### Question 1
#### Write a funtion to convert given CSV files to Dataframes
* Define function with name `csv_to_dataframe` which should accept `filepath` as a parameter.
* Function should return a dataframe.
* As we require a dataframe, type of return variable should be pandas dataframe.
* In case if we pass `filepath` which does not exist, function should raise FileNotFoundError.

### Question 2
#### Write a function to merge two dataframes on given column name
* Define function with name `merge_dataframe` which should accept `dataframe1`, `dataframe2`(dataframes to be merged), `column_name`(as string) as a parameter.
* Function should return a dataframe.
* As we require a dataframe, type of return variable should be pandas dataframe.
* In case if we pass `column_name` which does not exist, function should raise KeyError.


### Question 3
#### Write a function to convert datatype of given variables to "category"
* Define function with name `dtype_category` which should accept `dataframe` and `list of columns` as parameters.
* Function should return a dataframe with type of given columns changed to "category".
* As we require a dataframe, type of return variable should be `pandas dataframe`.
* In case if we pass column name which does not exist, function should raise KeyError

### Question 4
#### Write a function to count number of "categorical variables"
* Define function with name `categorical_variable_count` which should accept `dataframe` as parameter.
* Function should return count of categorical variables.
* As we require count, type of return variable should be integer.
* In case if we pass dataframe which does not exist, function should raise NameError

### Question 5
#### Write a function to check variance of numeric columns of a dataframe, and if variance is lower than given threshold, drop the column
* Define function with name `var_check` which should accept `dataframe`, `threshold` (int) as parameter.
* Function should drop the the rejected columns and return a list of dropped variables.
* As we require list, type of return variable should be list.

### Question 6
#### Write a function to plot boxplots for all numeric variables
* Define function with name `boxplot` which should accept `dataframe`, `column_list` (of variables to be plotted) as parameters.
* Function should return boxplots of numeric variables.
* As we require plot, type of return variable should be matplotlib object.
* In case if we pass column name which does not exist, function should raise KeyError