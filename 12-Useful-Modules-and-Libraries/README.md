# Demos of Useful Modules and Libraries
Python offers a vast array of modules and packages that can be imported for various uses. Initially, let us explore three commonly utilized modules/packages:
- Random Module
- tqdm Library
- numpy and pandas Libraries

# Random Modules
Typically, when beginning to use a new module that we have not utilized previously, it is advisable to start by consulting the "Documentation" provided by the module's creators. For instance, the random module, developed by Python itself, has its official documentation available at this link: https://docs.python.org/3/library/random.html.

The steps to make reading documentation less daunting include:
**Step 1** Understand the purpose of the module.
**Step 2** Identify the various methods and functionalities offered by the module.
**Step 3** Review the provided usage examples.
**Step 4** Attempt to apply these examples in practice.

# tqdm Libraries
In practical applications, our programs may take an extended period to run, particularly when executing loops. It can be beneficial to know how much time has elapsed for each loop iteration and estimate the remaining duration until completion.

Fortunately, there exists a library named tqdm that is readily available in Google Colab without the need for manual installation. One can learn the basic usage of this library by consulting its Documentation, which is accessible via this link: https://tqdm.github.io/.

# Numpy and Pandas Libraries
Individuals pursuing a career in Data Science must undoubtedly become proficient in using libraries such as numpy and pandas.
### 1. Numpy Libraries
Numpy is a library designed specifically for handling numerical data, allowing for the manipulation of complex numerical data structures across any dimensionality (1D, 2D, 3D, ... N-dimensional). Prior to utilization, it is requisite to import the library. Given its widespread popularity, Google Colab has pre-installed this package, thereby simplifying the process to merely importing it for use. It is customary to abbreviate its name as np during import.
```
import numpy as np
```
1) Numpy stores numbers in a structure called ndarray, short for N-Dimensional Array, where "Array" can be colloquially understood as "arranging items".
    - Arranging items in a single line (1D) is referred to as a 1D-Array, for example:
    ```
    my_array = np.array([55, 69, -31, 44, 122345])
    ```
    - Arranging items in rows and columns (2D) is called a 2D-Array, for example:
    ```
    my_matrix = np.array([[1,2,3],
                         [4,5,6]])
    ```
2) It is possible to perform statistical calculations on numbers within an Array, such as 
```
np.sum(my_array), np.mean(my_array)
```
3) Two Arrays can be added, subtracted, multiplied, and divided, provided that the "shape" (shape) of the Arrays is compatible.

### 2. Pandas Libraries
Pandas, on the other hand, is a library tailored for working with tabular data. It is capable of efficiently handling tables, even those extending to tens of millions of rows. Prior to its utilization, it is necessary to import the library. Owing to its significant popularity, Google Colab has pre-installed this package, thereby enabling immediate usage upon import. It is customary to abbreviate its name as pd.
```
import pandas as pd
```
1) **Pandas** stores table data within a structure known as DataFrame, hence variables containing this structure are commonly named with df.
2) Files in .csv (comma-separated values) format can be read using the command:
```
df = pd.read_csv("file_path")
```
3) Displaying the top 10 rows is achieved with the command:
```
df.head(10)
```
4) The shape (number of rows and columns) can be determined using the command:
```python
df.shape # No parentheses are needed as it requests an "Attribute" rather than a method.
```
5) Selecting a single column can be done with the command:
```
df["column_name"]
```
6) If a column contains numerical data, statistical calculations can be performed
```
df["age"].mean(), df["salary"].sum()
```
7) Additional functionalities applicable to DataFrame and Series can be explored in the Documentation.