#List:
list=[1,2,3,4,1,5,1,3,1,3]
list_1=[1,2,3,4,5,6,7,8,9]
print(type(list))
print(list)
print(list[0:])
print(list[0:len(list)])
print(list[0:2])
print(list[2:4])
list[2] = "Rudra"
print(list)
list.remove("Rudra")
list.append("This is my work")
print(list)
list_1.sort()
print(list_1)
list_1.sort(reverse=True)
print(list_1)
list_1.sort(reverse=True)
print(list_1)
list_1.reverse()
print(list_1)
list_1.reverse()
print(list_1)
list.pop(0)
print(list)
list.clear()
print(list)

#2-D list
list_2=["Piyush","Shukla"]
list_3=[1,2,3,4,5,6,7]
list_4=[22.3,44.3,43.43,34.3]
list_5=[list_2,list_3,list_4]
print(list_5)
print(list_5[0])
print(list_5[0][0])

#Tuple:
tuple_1=("Piyush","Sakshi","Dark")
print(tuple_1)
print(tuple_1.count("Piyush"))
print(tuple_1.index("Piyush"))

for x in tuple_1:
    print(x)
if "Piyush" in tuple_1:
    print("He is here")


#Sets:
utensils = {"fork","spoon","knife","butcher-knife","bowl"}
dishes = {"plate","bowl","cup","knife"}
print(utensils)
print(dishes)

utensils.add("glass")
utensils.pop()
x_1=utensils.copy()
print(x_1)
dishes.update(utensils)
print(dishes)

dinner_table = utensils.union(dishes)
print(dinner_table)


print(utensils.difference(dishes))
print(utensils.difference_update(dishes))
print(utensils)

print(utensils.intersection(dishes))


for x in dishes:
    print(x)


#Dictionary:
capitals = {"USA":"Washington DC",
            "INDIA":"New Delhi",
            "CHINA":"Beijing",
            "RUSSIA":"Moscow"}
print(capitals)
print(capitals["USA"])
print(capitals["INDIA"])

print(capitals.keys())
print(capitals.values())
print(capitals.get("INDIA"))
capitals_copy = capitals.copy()
print(capitals_copy)
print(capitals.update({"USA":"New York","INDIA":"Mumbai"}))
print(capitals)
print(capitals.pop("USA"))
print(capitals)
print(capitals.fromkeys("USA"))
print(capitals.popitem())
print(capitals)
print(capitals.setdefault("CHINA"))
print(capitals.setdefault("USA"))
print(capitals.items())

for keys,values in capitals.items():
    print(keys,values)

"""The Most important part is:
    1) list,sets,dictionaries are mutable.
    2) tupple and string are immutable.  """

#Index Operator:
#The index operator is used to access a specific element in a list, tuple, or string.
#It is denoted by square brackets [] and the index of the element to be accessed is placed

name = "Piyush Shukla"
if (name[0].isupper()):
    name = name.lower()
    print(name)

if (name[0:6].isalpha()):
    name = name.count("P" and "p")
    print(name)

if (name=="piyush shukla"):
    print("Hello, Piyush Shukla!")
else:
    print("Hello, Stranger!")
