# what is functional programming 

Functional programming is a style (or "paradigm" if you're pretentious) of programming 
where we compose functions instead of mutating state (updating the value of variables).


Functional programming is more about declaring what you want to happen, rather than how you want it to happen.
Imperative (or procedural) programming declares both the what and the how.


## Immutability 

In FP, we strive to make data immutable. Once a value is created, it cannot be changed. Mutable data
on the other hand, can be changed after its created.

# Who cares 

Immutable data is easier to think about and work with. When 10 different function has access to the same variable, and you are
debbugging a problem with that variable you have to consider the possibility that any of those functions could have changed the value.

When a variable is immutable, you can be sure that it hasn't changed since it was created. It's a helluva lot easier to work with.

Generally speaking, immutability means fewer bugs and more maintainable code.

# Tuples vs Lists 

Tuples and lists are both ordered collections of values, but tuples are immutable and lists are mutable.

You can append to a list, but you can not append to a tuple. You can create a new copy of a tuple using values from an existing tuple, but you can't change the existing tuple.


Functional programming aims to be declarative. We prefer to declare what we want the computer to do, rather than muck around with the details of how to do it.

Let's take an extreme example and pretend we wanted to style a webpage with CSS (Obviously a hypothetical because, well, why would anyone want to work on the frontend???)

# Declarative styling 

The following CSS change all buttons elements to have red text 

`button{color:red}`

It does not execute line-by-line like an imperative language. Instead, it simply declares the desired style, and it's up to a web browser to figure out how to apply and display it.

# Imperative Styling 

Unlike functional programming (and CSS), a lot of code is imperative. We write out the exact step-by-step implementation details. This Python script draws a red button on a screen using the Tkinter library:

`from tkinter import * # first, import the library
master = Tk() # create a window
master.geometry("200x100") # set the window size
button = Button(master, text="Submit", fg="red").pack() # create a button
master.mainloop() # start the event loop`


## Its math 

Functional programming tends to be popular amongst developers with a strong mathematical background. After
all a math equation inst procedural. It's declerative. Take the followinf example 

avg = Σx/N

To put this calculation in plain English:

* Σ is just the Greek letter Sigma, and it represents "the sum of a collection".
* x is the collection of numbers we're averaging.
* N is the number of elements in the collection.
* avg is equal to the sum of all the numbers in collection "x" divided by the number of elements in collection "x".

so the equation really just say avg is the average of all the numbers in collection "x". This math equation iis a 
declarative way of writing calculate the average of a list of numbers". Here's some imperative Python code that does the same thing.

`def get_average(nums):
    total = 0
    for num in nums:
        total += num
    return total / len(nums)`

However, with functional programming, we would write code that's a bit more declarative:

`def get_average(nums):
    return sum(nums) / len(nums)`


## Classes vs Functions 


I run into new developers who, after learning about classes, want to use them everywhere. They assume that because they learned about functions first, functions are somehow inferior.

Nope. They're just different.


If you're unsure, default to functions. I find myself reaching for classes when I need something long-lived and stateful that would be easier to model if I could share behavior and data structure via inheritance. This is often the case for:

Video games
Simulations
GUIs


## Debugging FP 

It's nearly impossible, even for tenured senior developers, to write perfect code the first time. That's why debugging is such an important skill. The trouble is, sometimes you have these "elegant" (sarcasm intended) one-liners that are tricky to debug:


`def get_player_position(position, velocity, friction, gravity):
    return calc_gravity(calc_friction(calc_move(position, velocity), friction), gravity)`


If the output of get_player_position is incorrect, it's hard to know what's going on inside that black box. Break it up! Then you can inspect the moved, slowed, and final variables more easily:


`def get_player_position(position, velocity, friction, gravity):
    moved = calc_move(position, velocity)
    slowed = calc_friction(moved, friction)
    final = calc_gravity(slowed, gravity)
    print("Given:")
    print(f"position: {position}, velocity: {velocity}, friction: {friction}, gravity: {gravity}")
    print("Results:")
    print(f"moved: {moved}, slowed: {slowed}, final: {final}")
    return final`


Once you've run it, found the issue, and solved it, you can remove the print statements.

## Toggle case


