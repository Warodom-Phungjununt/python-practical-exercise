# Object Oriented Programming (OOP)
### Why OOP ?
Previously, programming is a process of converting the input to output. However, converting the input to output process is not proper for some situation. Some situations are suitable for using the object as a center. For example,
```
Item (Class)
    attibutes
    {
        product_id
        name
        price
        stock_quantity
    }
    methods
    {
        .update_stock()
        ...
    }
```
##### Template for OOP Basics
```
class Animal():
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.water = 100
    
    def drink(self, amount):
        self.water += amount
    ...
```
##### Object from the class
```
animal_1 = Animal("Bobby", 20)
```
##### Using method()
```
animal_1 = drink(5)
```