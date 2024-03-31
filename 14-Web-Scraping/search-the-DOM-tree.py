# Introduction

### For mode information
### https://www.crummy.com/software/BeautifulSoup/bs4/doc/

### Start with importing "BeautifulSoup Library" and generate "BeautifulSoup object"
from bs4 import BeautifulSoup
import re

example = '''
<body>
  <h1>aHeader</h1>
  <div class="section1">
    <p>
      <a href="#">aLink</a>
    </p>
  </div>
  <div class="section2">
    <img src="img.jpg"/>
  </div>
</body>
'''

### Specify type of parser as htmal.parser
s = BeautifulSoup(example, 'html.parser')
print(s)

### Using prettify() for arranging data from html file
print(s.prettify())

# Search the Tree
### Find the Tag Name
### The easiest way to extract element from the HTML is using Tag Name
### For example, <h1> or <img> can be extracted by using .h1 or .img from BeautifulSoup Object
print(s.h1)
print(s.img)

### For extracting the element within the element
### .body.div can be used
print(s.body.prettify())
print('----------------')
print(s.body.div.prettify())

### Not only calling <h1> from .h1, but also calling find('h1')
print(s.h1)
print(s.find('h1'))

# Find Multiple Elements
###### If there are more than one tag within a DOM tree, find() function will find the latest result
print(s.div)
print(s.find('div'))
###### Finding all element
print(s('div'))
print(s.find_all('div'))
print(s('div')[1])

# Filters
###### Filter for element finding from message, attribute or class can be able to perform
# ค้นหาจากข้อความ
print(s.find(string='aHeader'))
# ค้นหาจาก attribute (href) ของ element 
print(s.find(href='#'))
# ค้นหาจาก attribute (class) ของ element 
print(s.find(class_='section1'))
# ค้นหาจากหลาย attributes
print(s.find(attrs={'class': 'section1'}))