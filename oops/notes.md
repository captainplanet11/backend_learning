## Object-Oriented Programming,
 or "OOP", is a pattern for writing clean and maintainable code. Not everyone agrees that object-oriented principles are the best way to write code, but, to be a good engineer, you should at least understand them.

In this course, we'll be coding the pieces of a real-time strategy game called "Age of Dragons". Players control armies of people, elves, orcs, and dragons and battle each other. It's similar to Age of Empires or StarCraft.

Assignment
One of the greatest sins when trying to write "clean code" is using misleading names for your variables and functions. Take a look at the destroy_wall function. Based on its name, you might assume that it destroys a single wall, but if you look closely, you'll see that it handles multiple walls.

The test suite expects a different function name. Take a look at the main_test.py file to see what it's looking for, and rename the function accordingly.

Additionally, try to rename the variables inside the function to be more descriptive. After passing the tests, take a look at the solution to see how we named everything.

# clean code 

Paradigms like object-oriented programming and functional programming are all about making code easier to work with and understand as the feeble humans we are. Code that's easy for humans to understand is called "clean code".

Clean Code Does Not

Make your programs run faster
Make your programs function correctly
Only occur in object-oriented programming

Clean Code Does

Make code easier to work with
Make it easier to find and fix bugs
Make the development process faster
Help us retain our sanity




# DRY CODE 

Another "rule of thumb" for writing maintainable code is "Don't Repeat Yourself" (DRY). It just means that, when possible, you should avoid writing the same code in multiple places. Repeating code can be bad because:

If you need to change it, you have to change it in multiple places
If you forget to change it in one place, you'll have a bug
It's more work to write it over and over again

## classes 

A class is a special type of value in an object-oriented programming language like Python. It's similar to a dictionary in that it usually stores other types inside itself.

`class Soldier:
    health = 5
    armor = 3
    damage = 2
`

Just like a string, integer or float, a class is a type, but instead of being a built-in type, your classes are custom types that you define.

An object is just an instance of a class type. For example:

health = 50
health is an instance of an integer type
aragorn = Soldier()
# aragorn is an instance of the Soldier type (class)


"Classes" are custom new types that we define as the programmer. Each new instance of a class is an "object".

# example 

`class Archer:
    health = 40
    arrows = 10

legolas = Archer()
bard = Archer()

print(legolas.health) # 40
print(bard.arrows) # 10

`
# Methods 

`
class Soldier:
    health = 5

    def take_damage(self,damage):
        self.health -= damage 


soldier_one = Soldier()
soldier_one.take_damage(2)
print(soldier_one.health)
`



# Method Return values 

class Soldier:
    armor = 2
    num_weapons = 2 

    def get_speed(self):
        speed = 10 
        speed -= self.armor 
        spped  -= self.num_weapons 
        return speed 

soldier_one  = Soldier()
print(soldier_one.get_speed())

# Methods vs Functions 

You know what a function is. A method has all the same properties as a function, but it is tied directly to a class and has access to all its properties.

A method automatically receives the object it was called on as its first parameter.

`
class Soldier:
    health = 5

    def take_damage(self,damage,multiplier):
        damage = damage * multiplier
        self.health -= damage 

dalinar = Soldier()
damage,multiplier =  30,3 
dalinar.take_damage(damage,multiplier)
`

# constructors 

It's rare in the real world to see class that defines property the way we have been doing it:

`class Soldier:
    name = "Legolas"
    armor = 2
    num_weapons = 2
`

It's more practical to use a constructor. In Python, if you name a method __init__, that's the constructor and it is called when a new object is created.

So, with a constructor, the code would look like this:

` class Soldier:
    def __init__(self,name,armor,num_weapons):
        self.name = name
        self.armor = armor
        self.num_weapons = num_weapons
soldier = Soldier("Legolas", 5, 10)
print(soldier.name)
print(soldier.armor)
print(soldier.num_weapons)`


### Encapsulation 


Encapsulation is the practice of hiding complexity inside a "black box" so that it's easier to focus on the problem at hand.
The most basic example of encapsulation is a function. The caller of a function doesn't need to worry too much about what happens inside, they just need to understand the inputs and outputs.

`acceleration = calc_acceleration(initial_speed, final_speed, time)`


To use the calc_acceleration function, we don't need to think about every individual line of code inside the function. We just need to know that if we give it the inputs:

initial_speed
final_speed
time
Then it will give us the correct acceleration as an output.


# public and private 

By default, all properties and methods in a class are public. That means that you can access them with the . operator:

private data members are how we encapsulate logic and data within a class. TO make a property or method private, you just need 
to prefix it with two underscores.

### Abstraction 



Abstraction helps us handle complexity by hiding unnecessary details. Sounds like encapsulation, right? They're so similar that it's almost not worth worrying about the difference...almost.


# Abstraction vs Encapsulation 

** Abstraction is about creating a simple interface for complex behavior. It focuses on what's exposed.
** Encapsulation is about hiding internal state. It focuses on tucking implementation details away so no one depends on them.

Abstraction is more about reducing complexity, encapsulation is more about maintaining the integrity of system internals.


Abstraction is about reducing complexity. Creating good abstractions is particularly crucial when you're developing libraries for other developers to use. For example, the built-in pow function in Python is an abstraction that hides the complexity of calculating exponents.

pow isn't magic. Somewhere, code that does something like this exists and is called when you use pow:

`def pow(base,component):
    result  = 1
    for _ in range(exponent):
        result *=  base
    return result`


### Inheritance 

We've made it to the holy grail of object-oriented programming: inheritance. Non-OOP languages like Go and Rust allow for encapsulation and abstraction features as nearly every language does. Inheritance, on the other hand, tends to be unique to class-based languages like Python, Java, and Ruby.


## What is inheritance ?

Inheritance allows one class, the "child" class, to inherit the properties and methods of another class, the "parent" class.

This powerful language feature helps us avoid writing a lot of the same code twice. It allows us to DRY (don't repeat yourself) up our code.


**Here Cow is a "child" class that inherits from the "parent" class Animal:**

`class Animal:
class Cow(Animal)`




# when should I use Inheritence 

Inheritance is a powerful tool, but it is a really bad idea to try to overuse it. Inheritance should only be used when all instances of a child class are also instances of the parent class.

When a child class inherits from a parent, it inherits everything. If you only want to share some functionality, inheritance is probably not the best answer. Better to simply share some functions, or maybe make a new parent class that both classes can inherit from.

All cats are animals but not all animals are cats:


# Inheritance  hierarchy 

There is no limit to how deeply we can nest an inheritance tree. For example, a Cat can inherit from an Animal that inherits from LivingThing. That said, be careful! New programmers often get carried away.

An example of this with private properties. A child class cannot simply access a private property of its parent class. It has to use a getter. For example:


`class Wall:
    def __init__(self, height):
        self.__height = height

    def get_height(self):
        return self.__height

class Castle(Wall):
    def __init__(self, height, towers):
        super().__init__(height)
        self.towers = towers

    def get_tower_height(self):
        return self.get_height() * 2`




