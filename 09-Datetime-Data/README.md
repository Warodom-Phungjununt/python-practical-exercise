# Datetime Data

Datetime data is not initially installed with Python. Therefore, Using datetime data can be used by calling **datetime module**. Within the datetime module, there 4 data type for this module.

### 1. date
```
date(2024, 3, 28)
```
date(2024, 3, 28): Year 2024, Month March, and date 28.

### 2. time
```
time(20, 15, 30)
```
time(20, 15, 30): 20 hours, 15 minutes, and 30 seconds.

### 3. datetime
```
datetime(2024, 3, 28, 20, 15, 30)
```
datetime(2024, 3, 28, 20, 15, 30): Year 2024, Month March, date 28, 20 hours, 15 minutes, and 30 seconds.

### 4. timedelta
```
timedelta(days = 4, hours = 3, seconds = 32)
```
timedelta(days = 4, hours = 3, seconds = 32): Period of 4 days, 3 hours, and 32 seconds.

Furthermore, datetime module can be used with the aggregation, i.e.
- find the difference of datetime: datetime2 - datetime1
- compare the datetime: datetime2 > datetime1, datetime2 == datetime1
- Add with the period of time (future): datetime1 + timedelta
- Minus with the period of time (past): datetime2 - timedelta

# Converting String to Datetime
String can be converted to the Datetime type by using *.strptime()* which is come from _"string parse to time"_
```python
dt.datetime.strptime(original string, form of datetime which similar to the original string)
```
Type of format codes are:
- `%Y` : 4-digit A.D. year
- `%m` : 2-digit months
- `%d` : 2-digit days
- `%H` : 2-digit hours
- `%M` : 2-digit minutes
- `%S` : 2-digit seconds
- `%b` : 3-digit of abbreviation months (Jan, Feb, ..., Dec)
- `%B` : Full months (January, February, ..., December)
- `%a` : Abbreviation days (Sun, Mon, ..., Sat)
- `%A` : Full days (Sunday, Monday, ..., Saturday)

# Converting Time to String
Also, date, datetime, time, etc. are able to convert to string by using **strftime()** which is come from _"string from time"_
```python
datetime_object.strftime(desired string format)
date_object.strftime(desired string format)
time_object.strftime(desired string format)
```
