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
#print(s)

### Using prettify() for arranging data from html file
print(s.prettify())