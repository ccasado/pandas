import numpy as np
import pandas as pd

# 1. Object creation

# Creating a Series by passing a list of values, letting pandas create a default integer index:
series = pd.Series([1, 3, 5, 20, 9+1, np.nan, 30])
print(series)
"""
0     1.0
1     3.0
2     5.0
3    20.0
4    10.0
5     NaN
6    30.0
dtype: float64 
"""

# Creating a DataFrame by passing a NumPy array, with a datetime index and labeled columns:
dates = pd.date_range("20210416", periods=6)
print(dates)
"""
DatetimeIndex(['2021-04-16', '2021-04-17', '2021-04-18', '2021-04-19',
               '2021-04-20', '2021-04-21'],
              dtype='datetime64[ns]', freq='D')
"""

dataframe = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
print(dataframe)
"""
                   A         B         C         D
2021-04-16 -0.051929 -0.875676  0.660774  0.291489
2021-04-17  1.339421 -0.413208  0.203138  0.282237
2021-04-18  0.469639 -0.552956  0.734373  2.331192
2021-04-19 -0.100487 -0.737573 -0.520274  0.032894
2021-04-20 -0.276591  0.866722  0.942338  0.272999
2021-04-21  2.350279 -0.296165  0.533465 -0.613423
"""

# Creating a DataFrame by passing a dict of objects that can be converted to series-like.
dataframe2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20150204"),
        "C": pd.Series(1, index=list(range(5)), dtype="float32"),
        "D": np.array([3] * 5, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train", "test"]),
        "F": "foo",
    }
)
print(dataframe2)
"""
     A          B    C  D      E    F
0  1.0 2015-02-04  1.0  3   test  foo
1  1.0 2015-02-04  1.0  3  train  foo
2  1.0 2015-02-04  1.0  3   test  foo
3  1.0 2015-02-04  1.0  3  train  foo
4  1.0 2015-02-04  1.0  3   test  foo
"""

print(dataframe2.dtypes)
"""
A           float64
B    datetime64[ns]
C           float32
D             int32
E          category
F            object
dtype: object
"""

# 2. Viewing data

# Here is how to view the top and bottom rows of the frame:
print(dataframe2.head(2))
"""
     A          B    C  D      E    F
0  1.0 2015-02-04  1.0  3   test  foo
1  1.0 2015-02-04  1.0  3  train  foo
"""
print(dataframe2.tail(2))
"""
     A          B    C  D      E    F
3  1.0 2015-02-04  1.0  3  train  foo
4  1.0 2015-02-04  1.0  3   test  foo
"""


# Display the index, colums:
print(dataframe2.index)
#Int64Index([0, 1, 2, 3, 4], dtype='int64')
print(dataframe2.columns)
#Index(['A', 'B', 'C', 'D', 'E', 'F'], dtype='object')

# Shows a quick statistic summary of your data:
print(dataframe2.describe())
"""
         A    C    D
count  5.0  5.0  5.0
mean   1.0  1.0  3.0
std    0.0  0.0  0.0
min    1.0  1.0  3.0
25%    1.0  1.0  3.0
50%    1.0  1.0  3.0
75%    1.0  1.0  3.0
max    1.0  1.0  3.0
"""

# Sorting by an axis:
print(dataframe2.sort_index(axis=1, ascending=False))
"""
     F      E  D    C          B    A
0  foo   test  3  1.0 2015-02-04  1.0
1  foo  train  3  1.0 2015-02-04  1.0
2  foo   test  3  1.0 2015-02-04  1.0
3  foo  train  3  1.0 2015-02-04  1.0
4  foo   test  3  1.0 2015-02-04  1.0
"""

# 3. Selection

# Getting
# Selecting a single column, which yields a Series, equivalent to df.A:
print(dataframe2["A"])
"""
0    1.0
1    1.0
2    1.0
3    1.0
4    1.0
Name: A, dtype: float64
"""

# Selecting via [], which slices the rows.
print(dataframe2[0:3])
"""
     A          B    C  D      E    F
0  1.0 2015-02-04  1.0  3   test  foo
1  1.0 2015-02-04  1.0  3  train  foo
2  1.0 2015-02-04  1.0  3   test  foo
"""

# Selection by label

#For getting a cross section using a label:
print(dataframe.loc[dates[0]])
"""
A    0.819766
B   -0.183001
C    0.850259
D   -1.359568
Name: 2021-04-16 00:00:00, dtype: float64
"""

#Selecting on a multi-axis by label:
print(dataframe.loc[:, ["A", "B"]])

