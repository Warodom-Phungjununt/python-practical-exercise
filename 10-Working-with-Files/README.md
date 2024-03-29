Sometimes, reading and writing with files are needed for programming. Therefore, the correction of file path is needed to consider. Additional, there are 4 issues that need to be aware of:
1. Full and relative paths
2. Joining paths
3. Reading text files
4. Writing text files

# Full and Relative Paths
Path of files or folders can be specified by 2 ways:
1. Full Path 
```
/c/d/M/A/demo.ipynb
```
2. Relative Path 
```
./demo.ipynb
```
Noted: Files can be checked by using **os module**
```
import os
os.path.exists(file)
```

# Joining Path
Two or more file paths can be joined together by using **join() method**
```
import os
os.path.join(path1,path2,...)
```

# Reading Text File
Files can be accessed for their contents using the **open()** function. It is recommended to utilize the with statement in conjunction with this function to manage file reading scopes and to automatically close the file upon completion of reading, obviating the need for explicit invocation of the **.close()** method. This approach mitigates potential harm arising from inadvertent failure to close the file.
```
with open(file_path, mode='r') as f:
    #something with f
```
Reading with files can be performed by 3 ways
### 1. Reading all
```
content = f.read()
```

### 2. Reading each line
```
single_line = f.readline()
```

### 3. Reading each line until the end
```
all_lines = f.readlines()
```
The result will be a **_List Type_**

### Template for Reading
###### case 1: Print the first three lines
```
with open(file_path, mode='r') as f:
  for i in range(3):
    print(f.readline())
```
###### case 2: Convert to Dictionary
```
new_dict = dict()
for line in old_list:
  part = line.split(',')
  keypart = part[0]
  valuepart = part[1]
  new_dict[keypart] = valuepart
```
Dictionary comprehension can be also used
```
new_dict = {key: value for key, value in (line.split(',') for line in old_list)}
```
###### case 3: Reading first 3 lines of csv-file
```
with open(file_path, mode='r') as f:
  for i in range(3):
    print(f.readline())
```
###### case 4: Reading all of csv-file
```
with open(file_path, mode = 'r') as f:
  column = f.readline()
  all_rows = f.readlines()
```
###### case 5: Convert columns to the list of columns
```
column_list = [column_name.strip() for column_name in column.split(',')]
```
###### case 6: Convert 2D-dictionary to the list
```
new_dict = dict()
for line in all_rows:
  part = line.split(',')
  data0 = part[0]
  new_dict[data0] = {
      'data1':part[1],
      'data2':part[2],
      'data3':part[3],
      'data4':part[4],
      'data5':part[5],
      'data6':part[6].strip() == 'True' ## For removing \n
  }
  ```
# Writing Text Files
Content can be written to and saved in a file by altering the mode from 'r' (read) to 'w' (write). There are two primary methods for writing content to a file as follows:
### 1. Writing all in one time
```
f.write("message")
```
### 2. Writing each line until the end
```
f.writelines("text_line")
```
### Template for Writing
###### case 1: Writing to Text-File
```
with open(file_path, mode = 'w') as f:
  f.write(message)
```
###### case 2: Converting 2D-Dictionary to List
```
new_list = []
for id, info in old.items():
  values = info.values()
  values = [str(v) for v in values]
  result = ','.join(values)
  result = id + ',' + result + '\n'
  new_list.append(result)
```
###### case 3: Generate csv-file by using .writelines()
```
header = 'head1,head2,head3,head4,head5\n'
with open(file_path, mode='w') as f:
  f.write(header)
  f.writelines(new_list)
```
###### case 4: Append new list to old list
```
more_new_list = []
for id, info in more.items():
  values = info.values()
  values = [str(v) for v in values]
  result = ','.join(values)
  result = id + ',' + result + '\n'
  more_new_list.append(result)

with open(file_path, mode='a') as f:
  f.writelines(more_new_list)
```