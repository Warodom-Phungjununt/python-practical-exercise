# Error Handling
In the process of coding, errors or informally referred to as "bugs," may arise, which are typically categorized into two types:
### 1.Syntax Errors
These occur due to incorrect code writing, such as forgetting to close a parenthesis, misspelling commands, or improper indentation, among others.
### 2.Exceptions
Even with correct syntax, the execution may halt due to errors that prevent the code from running further, like division by zero, using an undefined variable, or incorrect type input.

Syntax errors must be corrected for the code to run properly, while exceptions necessitate the implementation of error handling mechanisms within the code to specify how the program should continue in case these errors occur.

# Try-Statement
If any mistakes occur, users can use the **_try statement_** to handle potential errors. The template for a try statement is as follows:
```python
try:
    #code
    #...
except:
    # what user want to do if there is an error
    # while trying until the code cannot run anymore
```
**_Else_** clause can be added to specify actions to be taken in the absence of errors, and a **_finally_** clause can be employed to define statements that should be executed at the conclusion, regardless of whether an error occurred or not.
```python
try:
    #code
    #...
except:
    # what user want to do if there is an error
    # while trying until the code cannot run anymore
else:
    # specify actions to be taken in the absence of errors
finally:
    # define statements that should be executed at the conclusion
```