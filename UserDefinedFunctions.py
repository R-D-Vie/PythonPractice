def greet_twice():
    print("Hello")
    print("Hello")


greet_twice()

#add docstring for help on user defined functions


def greet_twice():
    """Print the string 'Hello' two times"""
    print("Hello")
    print("Hello")


help(greet_twice)

#another example
def caesar_quote():
    """Print the Latin version of 'I came, I saw, I conquered'"""
    print("Veni, vidi, vici")


caesar_quote()

#further example


def my_function():
    """Print the string 'This is a function'."""
    print("This is a function")


my_function()

#parameters


def add_sub(num1, num2, num3):
    """add_sub does the following:
    Add the first two parameters
    Subtract the third paramter
    Print the result"""
    print(num1 + num2 - num3)


add_sub(10+5, 20//4, 5*10)


def subtract(num1, num2):
    """Subtract the second parameter from the first"""
    print(num1 - num2)


subtract(5, 2)
subtract(2, 5)
subtract(num2=2, num1=5)


def parameter_types(param1, param2, param3, param4):
    """Takes four parameters
    Print the type of each element"""
    print("The type of {} is {}".format(param1, type(param1)))
    print("The type of {} is {}".format(param2, type(param2)))
    print("The type of {} is {}".format(param3, type(param3)))
    print("The type of {} is {}".format(param4, type(param4)))


parameter_types(1, 5.9, "Beatles", False)


def parameter_types(param1, param2, param3, param4):
    """Takes four parameters
    Print the type of each element"""
    print("The type of {} is {}".format(param1, type(param1)))
    print("The type of {} is {}".format(param2, type(param2)))
    print("The type of {} is {}".format(param3, type(param3)))
    print("The type of {} is {}".format(param4, type(param4)))


parameter_types(range(10), "", parameter_types, 45)

#explaining errors


def addition(num1, num2):
    """Add the two parameters together
    Use try/except to catch any type errors"""
    try:
        print(num1 + num2)
    except TypeError:
        print("Please pass the function two numbers")


addition(5, "cat")


def color_sentences(white, red, green):

print("{} are white. {} are red. {} is green.".format(white, red, green)
          color_sentences("Clouds", "Firetrucks", "Grass")

          def division(num1, num2):
          try:
          print(num1 / num2)
          except ZeroDivisionError:
          print("Division by zero is not allowed")

#variable scope - When a variable is declared inside a function, it has local scope
def function_1():
    my_var="Hello"
    print(my_var)

def function_2():
    my_var="Bonjour"
    print(my_var)

def function_3():
    my_var="Hola"
    print(my_var)

    function_1()
    function_2()
    function_3()
    
#When a variable is declared in the main program, it has global scope
greeting="Hello"

def say_hello():
    """Print a greeting"""
    print(greeting)

say_hello()

      greeting="Hello"

      def say_hello():
      """Print a greeting"""
      greeting="Bonjour"
      print(greeting)

      say_hello()
      print(greeting)

#use of global keyword
      greeting="Hello"

      def say_hello():
      """Demonstrate how to use the global keyword"""
      global greeting
      greeting="Bonjour"
      print(greeting)

      say_hello()
      print(greeting)

      my_var=5
      def add_5():
      print(my_var + 5)
      add_5()

      my_var=0
      def change_var():
      global my_var
      my_var += 1
      change_var()

#returning values
      def add_five(num):
      """Add five to the parameter num"""
      return(num + 5)

      new_number=add_five(10)
      print(new_number)

#can return any values
      def return_int(num1, num2):
      """Return the floor division of num1 divided by num2"""
      return(num1 // num2)

      def return_float(num1, num2):
      """Return num1 divided by num2"""
      return(num1 / num2)

      def return_string(string):
      """Return the value of string appended to 'Hello' """
      return("Hello" + string)

      print(return_int(10, 3))
      print(return_float(10, 3))
      print(return_string(" friend"))

#side effects
      my_num=0

      def add_5(num):
      """Receive a number, add 5 tot the number, and
    return the new number"""
      return(num + 5)

      for i in range(10):
      my_num=add_5(my_num)
      print(my_num)


