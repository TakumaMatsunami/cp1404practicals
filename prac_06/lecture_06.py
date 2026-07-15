"""
Lecture 6, Week 6

Classes and Object-Oriented Programming

Object-Oriented Programming
    focused on creating objects instances of classes
    object is an entity that contains data and procedures
        data known as data attributes
        procedures known as methods
            methods are functions that perform operations on the data attributes
    encapsulation
        combining single data and code into single object

Classes
    used to create objects
    code that specifies the data attributes and methods of particular type
    instance
        object created from a class

PEP8 for Class
    class follows the CapWord convention
        StudentRecord
    method follows the same as functions
        set_value
    public attributes follows no leading underscore
    non public attributes follows leading underscore
        non public when it cannot be reached by the user
        _is_stolen

Private Attributes
    can use double underscore if front of any variable
        for avoiding naming clashes with subclasses
    mangling the name to include the class

Class and Standard Methods
    __init__
        a class constructor that executed when instance of that class created
        initalize the objects data attributes and assign itself to the object thats created
        usually the first method in class definition
        just like the main() version of the class
    self
        references the specific object that method invoked in
        required as the first parameter in every methods
    __str__
        python can run a string method when you want to print an object
        this must return a string
    __repr__
        when trying to print out a list of custom object
        will not invoke the str method so define using repr
        a class with repr but no str, the repr will work as the string

Key Terminology
    Class = class HelloWorld
    Object = specific instance of particular class
    Method = def build(self):
    reference to this instance = self.
    Inheritance = (App)
    Call Method = .run()

Class's Responsibility
    things are for knowing = data attributes
    actions are for doing = methods
    usually stored in a module file then imported when needed

Client Code and Class Code
    if imports it will read through the entire module code (class code)
    so if contains normal program it will also run these
    to prevent running these use...
        if __name__ = '__main__':

Class Variables
    when all object of class to share common constant/variable
    not and instance variable
    place the variable before __init__

attrgetter
    when u want to sort item, using the attribute

Why use class
    class is convenient representation of smt
    can buildmore complex systems out of these
"""

# Write a list comprehension to produce a new list containing only the products that are on sale.

products = [["Phone", 340, False], ["PC", 1420.95, True], ["Plant", 24.5, True]]
on_sale_products = [product for product in products if product[2]]
print(on_sale_products)


# Class Sample

class Plant:
    def __init__(self, name="", height=0.0, growth_rate=1.0):
        self.name = name
        self.height = height
        self.growth_rate = growth_rate

    def feed(self, amount_of_water):
        self.height += amount_of_water * self.growth_rate