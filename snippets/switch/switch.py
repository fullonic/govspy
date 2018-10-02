def input_():
    return int(input())


number = input_()
if number == 8:
    print("Oxygen")
elif number == 1:
    print("Hydrogen")
elif number == 2:
    print("Helium")
elif number == 11:
    print("Sodium")
else:
    print("I have no idea what %d is" % number)


# Alternative solution
number = input_()
db = {1: "Hydrogen", 2: "Helium", 8: "Oxygen", 11: "Sodium"}
print(db.get(number, "I have no idea what %d is" % number))
