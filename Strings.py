#string length

my_string = "Hello"
length = len(my_string)
print(length)

#reference a character
my_string = "Hello!"
character = my_string[1]
print(character)

my_string = "Hello!"
character = my_string[-1]
print(character)

#triple quotes (for whitespace preservation)
long_string = """Notice how this weird looking
    string is being
        printed."""
print(long_string)

#the 'in' operator returns a boolean value
my_string = "The brown dog jumps over the lazy fox."

print("dog" in my_string)

#the slice operator for strings
my_string = "The brown dog jumps over the lazy fox."
my_slice = my_string[4:9]

print(my_slice)


my_string = "The brown dog jumps over the lazy fox."
my_slice = my_string[0:len(my_string)]

print(my_slice)

#escape character - new line
my_string = "Hello\nworld"
print(my_string)

#unicode example
my_string = "Hello\u041bworld"
print(my_string)

#quotes inside quotes
my_string = "And then she said, 'Hi there.'"
print(my_string)

#string max function
my_string = "xyz321"
print(max(my_string))

#if statement, min/max strings
string1 = ""
string2 = ""

if max(string1) > max(string2):
    print("string1 has the biggest character")
else:
    print("string2 has the biggest character")

#the strip method - only removes elements from the beginning or end of a string
string1 = "Hello world"
string2 = "world"
print(string1.strip(string2))

#starts with
my_string = "this is a string"
my_bool = my_string.startswith("this")
print(my_bool)

my_string = "this is a string"
my_bool = my_string.startswith("is", 2)
print(my_bool)

#the replace method
my_string = "dog mouse fish dog bear"
new_string = my_string.replace("dog", "cat")
print(new_string)

my_string = "dog mouse fish dog bear"
new_string = my_string.replace("dog", "cat", 1)
print(new_string)

#find
string1 = "The brown dog jumps over the lazy fox."
string2 = "brown"
print(string1.find(string2))

#the upper/lower method - convert to upper case
my_string = "the big brown dog"
print(my_string.upper())

my_string = "THE BIG BROWN DOG"
print(my_string.lower())

#the capitalize method
my_string = "the big brown dog"
print(my_string.capitalize())

#title
my_string = "the big brown dog"
print(my_string.title())

#terating over a string
my_string = "Hello world"
for char in my_string:
    print(char)

my_string = "\u25A3\u25A8\u25D3\u25CC\u25A2"
for char in my_string:
    print(char)

my_string = "\u25A3\u25A8\u25D3\u25CC\u25A2"
for char in my_string:
    print(my_string)

#iteration - while
my_string = "Calvin and Hobbes"
length = len(my_string)
i = 0

while i < length:
    print(my_string[i])
    i += 1

#comparing strings - boolean
string1 = "It's Friday!"
string2 = "It's Friday!"
print(string1 == string2)

string1 = "It's Friday!"
string2 = "It's Monday."
print(string1 != string2)

#is replaces ==
string1 = "It's Friday!"
string2 = "It's Friday!"
print(string1 is string2)

#is not replaces !=
string1 = "It's Friday!"
string2 = "It's Monday."
print(string1 is not string2)

#alphabetical order
string1 = "apple"
string2 = "zebra"
if string1 < string2:
    print("{} comes before {}".format(string1, string2))
elif string1 is string2:
    print("{} is the same as {}".format(string1, string2))
else:
    print("{} comes after {}".format(string1, string2))

#String interpolation is the process of putting the value of a variable inside of a string
arms = 2
fingers = 10
print("I have " + str(arms) + " arms and " + str(fingers) + " fingers.")

verb = "jumps"
adjective = "lazy"
print("The brown dog ", verb, " over the ", adjective, " fox.")

#format method
var1 = "today"
var2 = "luckiest"
print("Yet {} I consider myself the {} man on the face of this earth.".format(var1, var2))

var1 = "Up"
var2 = "away"
my_string = f"{var1}, up and {var2.upper()}."
print(my_string)

name = "Calvin"
age = 6
occupation = "student"
sentence = f"My name is {name}. " \
           f"I am {age} years old. " \
           f"I am a {occupation}."
print(sentence)

name = "Calvin"
age = 6
occupation = "student"
sentence = f"""My name is {name}.
           I am {age} years old.
           I am a {occupation}."""
print(sentence)

var1 = "blue"
var2 = "Roses"
var3 = "red"
phrase = "%s are %s, violets are %s." % (var2, var3, var1)
print(phrase)
