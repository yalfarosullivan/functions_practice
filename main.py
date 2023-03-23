# Implement a function that will flatten and sort an array of integers in ascending order, and which adheres to a functional programming paradigm.

def flatten_and_sort(array):
    arr = []
    for item in array:
        for i in item:
            arr.append(i)
    return sorted(arr)


# How does this solution ensure data immutability?
# The original list doesn't change. It adds the sorted and flattend list to a new list.

# Is this solution a pure function? Why or why not?
# It  does not change the original list or create side effects. 

# Is this solution a higher order function? Why or why not?
# Yes, it is returing a sorted()

# Would it have been easier to solve this problem using a different programming style?
# No, as this is the simple way to solve problem.

# Why in particular is functional programming a helpful paradigm when solving this problem?
# it is straightforward / pure.

# Watto needs a new system for organizing his inventory of podracers. 

# Help him do this by implementing an Object Oriented solution according to the following criteria.

# First, he'll need a general Podracer class defined with max_speed, condition (perfect, trashed, repaired) and price attributes. 
class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

# Define a repair() method that will update the condition of the podracer to "repaired".
    def repair(self):
        self.condition = "repaired"
    
# Define a new class, AnakinsPod that inherits the Podracer class, but also contains a special method called boost that will multiply max_speed by 2.
class AnakinsPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super.init(max_speed, condition, price):
  
    def boost(self):
        self.max_speed *= 2
    
# Define another class that inherits Podracer and call this one SebulbasPod. 
# This class should have a special method called flame_jet that will update the condition of another podracer to "trashed".
class SebulbasPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super.init(max_speed, condition, price):
  
    def flame_jet(self,other):
        other.condition = "trashed"


# How does this solution demonstrate the four pillars of OOP? 
# Encapsulation, Abstractiion, Inheritance, Polymorphism 

# It used Encapsulation, Inheritance and Polymorphism. Encapsulation allowed 
# others classes to be hidden from the Podracer attributes. SebulasPod and AnakinsPod were 
# able to be resuse the Podracer's attributes, allowed by Inheritance. flame_jet and boost 
# added functionality to items that were shared with Podracer, using Polymorphism. 

# Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
# This was the best w ay to breakdown the code and keep it organized.

# How in particular did Object Oriented Programming assist in the solving of this problem?
# The data was grouped into clasess. It allowed for polymorphism and inheritance by creating the common attributes,
# extending int other classes from the Podracer class.

