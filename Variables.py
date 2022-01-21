#Variables are used to store a value, and these values have a data type. Data types describe the kind of information that is being stored.
my_variable = "Hello world"
print(my_variable)

#example - fundamentals
variable_1 = "Python fundamentals are very useful"
variable_2 = variable_1
print(variable_2)

#overwriting variables
my_variable = "Hello world"
print(my_variable)
my_variable = "Goodbye world"
print(my_variable)

#strings - you can use double or single quotation marks
string_variable = "This is a string"
second_string = 'This is a string also'
print(string_variable)
print(second_string)

#boolean variables (are case sensitive and must be uppercase)
boolean_variable = True
print(boolean_variable)

#integers (often called ints) are whole numbers
#Floating point numbers (often called floats) are numbers with a decimal.
float_variable = 50.0
print(float_variable)

#the output for this code will be 'True' - all four variables have the value 'True' by the end of the program because variables are dynamic and can change the types of data they hold
string_variable = "This is a string"
float_variable = 3.14159
int_variable = 42
boolean_variable = True

string_variable = boolean_variable
float_variable = string_variable
int_variable = float_variable
boolean_variable = int_variable

print(int_variable)

