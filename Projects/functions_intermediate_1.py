# Create beCheerful().  Within it, print string "good morning!" 98 times.
print("*" * 80)


def beCheerful(name='', repeat=98):
    print(f"good morning {name}\n" * repeat)


beCheerful()
beCheerful(name="john")
beCheerful(name="michael", repeat=5)
beCheerful(repeat=5, name="kb")
beCheerful(name="aa")


def rand_int(max=100, min=0):
    return int(random.random() * (max-min) + min)


# helpful tips for the next assignment
import random

print(random.random())  # returns a random floating number between 0.000 to 1.000
print(random.random() * 50)  # returns a float between 0.000 to 50.000
int(3.654)  # returns 3
round(3.654)  # returns 4
for x in range(100):
    print(rand_int(min=50, max=100))