# Here we are importing math into our file
import math
# Here we are creating a class called Calcu
class Calcu:
    # Here we make a method to work out the sq root
    def find_sqrt(self, num2):
        return math.sqrt(num2)
    # Here we make a method to round up
    def find_ceil(self, num2):
        return math.ceil(num2)
    # Here we make a method to round down
    def find_floor(self, num2):
        return math.floor(num2)

# Here we are creating an object from the Calcu class
simple_calcu = Calcu()

# Here we are just printing using the methods created to see if they work.
print(simple_calcu.find_ceil(102.8))
print(simple_calcu.find_floor(1001.4))