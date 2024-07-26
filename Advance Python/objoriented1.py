#creation of a class
class cl:
    name=""
    age=0
    def study(self):
        print("study")
        self.sleep()
    def sleep(self):
        print("sleep")
        
#inheritence in classes
class a:
    def dhoe(self):
        print("hello a")
class b(a):
    def sb(self):
        print("b is inherited from a, single inheritence")
class c(a):
    pass


#polymorphism- function overloading and function overriding4

#function overloading- in this the last function is considered made with the samne names
def d(name, age):
    print(name,age)
def d(name,age,classs):
    print("overloaded")
    
#polymorphism overriding
class bird:
    def intro (self):
        print("there are many type of birds")
    def flight(self):
        print("some birds can fly some cannot")
class sparrow(bird):
    
    def flight(self):
        print("can fly ")
class ostrich(bird):
    def flight(self):
        print("cannot fly ")

#encapsulation
class sh:
    def __init__(self):
        self.__name = "shreyaaaaa"
    
    # Getter method
    def get_name(self):
        return self.__name
    
    # Setter method
    def set_name(self, name):
        self.__name = name

class data(sh):
    def show(self):
        print("this is show method")
        print("Name:", self.get_name())  # Use the getter method to access __name

#object creation
ob=cl()
ob.study()

#inheritence
two=c()
two.dhoe()
#two.sb() error

#polymorphism overloading
d("shreya",20,"4th yr")
#polymorphism overriding is th eprocess of reimplementing a method in the child class. this is particularly useful in cases where the method inherited from the parent class doesnot quite fit in the child class
ostric=ostrich()
ostric.flight()


#encapsulation

# Usage
de = data()
de.show()  # Display the name using the show method

# Setting a new name using the setter method
de.set_name("newname")
de.show()  # Display the new name using the show method
