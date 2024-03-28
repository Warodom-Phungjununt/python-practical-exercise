# List Comprehensions

### 1. Without Condition
```
new_list = [new value from v for v in old_list]
```

### 2. With Condition If
```
new_list = [new value from v for v in old_list **_if condition_**]
```

### 3. With Condition If-Else
```
new_list = [new value **_if_ true condition _else_ false condition** from v for v in old_list]
```

There are two more interested used case for the list comprehensions
1. More than 1 condition
```
python
profits = [-1, 3, 0, 1, 25, 4, -5]
performance = ["กำไร" if p > 0 else "เท่าทุน" if p == 0 else "ขาดทุน" for p in profits]
print(performance)
```
Result: `['ขาดทุน', 'กำไร', 'เท่าทุน', 'กำไร', 'กำไร', 'กำไร', 'ขาดทุน']`

2. Flatten List
```python
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9, 10]]
flattened_list = [item for sublist in nested_list for item in sublist]
print(flattened_list)
```
Result: `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`