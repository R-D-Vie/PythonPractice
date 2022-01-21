# for loops: example 1
import turtle
for i in range(5):
    print("Hello")

#for loops: example 2
for i in range(10, 0, -1):
    print("Loop #" + str(i))

#while loops: example 1

count = 0  # counting variable
while count < 5:
    print("Hello")
    count = count + 1

#while loops: example 2
my_var = 0
while my_var < 10:
  my_var += 1
  print(my_var)

#while loops: example 3
total = 0
while True:
    total = total + 1
    if total > 100:
        break
    print(total)

#nested loops: example 1
for row in range(10):
    for column in range(10):
        # By adding `end=""` to the print function, Python will not go to the next line.
        print("#", end="")
    print("")  # add new line character

#nested loops: example 2
for i in range(4):
    print("&&")
    for j in range(3):
        print("*")

