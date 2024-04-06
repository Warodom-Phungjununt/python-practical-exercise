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

s = BeautifulSoup(example, 'html.parser')
# print(s)
# print(s.prettify()) 

# 2. Traverse the DOM tree

# 2.1 Going Down
print(s.body.contents)
# Using ".children" for the iteration
for child in s.body.children:
  print('----------')
  print(child)

# 2.2 Going Up
# Call the body that include div
print(s.div.parent)
# Call the previous sibling
print(s.div.previous_sibling)
print(s.div.previous_sibling.previous_sibling)
# Call the next sibling
print(s.div.next_sibling)
print(s.div.next_sibling.next_sibling)

# 2.3 Going Back and Forth
# Calling the element within the tag
# Call the previos element
# Find the difference between "previous_element" and "previous_sibling"
print(s.div.previous_element)
print(s.div.previous_element.previous_element)
# Call the next element
print(s.div.next_element)
print(s.div.next_element.next_element)

# 2.4 Go Around with "find"
print(s.div.find_previous_sibling())
# s.div.previous_sibling
# '\n'
print(s.find('div', class_='section2') \
  .find_previous_sibling('h1'))
print(s.a.find_next())
# s.a.next_element
# 'aLink'
print(s.a.find_next('img'))