# Key and value

# ordered: indexed

# changeable: change, add, remove

# Does not allow duplicates: no key can be the same

chase = {
    "Name": "Chase",
    "Pet": "True",
    "Color": "white",
    "Height": 6
}
chase.update({"Height": 5})
chase.pop("Pet")
x = chase
print(x)

