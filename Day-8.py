#Lambda Function:
#A lambda function is a small anonymous function that can take any number of arguments, but can only
# have one expression.
#The syntax of a lambda function is: lambda arguments : expression

add=lambda x,y:x+y
print(add(5,4))

age_check=lambda n: True if n>=18 else False
print(age_check(12))

name=lambda First_name,Last_name:First_name+" "+Last_name
print("Piyush","Shukla")

#Sort Method:
#The sort() method sorts the items of a list in a specific order.
#The sort() method takes one argument: reverse, which is an optional argument that defaults to False

students=["Piyush","Anant","Aman","Priya"]
students.sort(reverse=True)

for i in students:
    print(i)

print("\n")
students.sort()

for i in students:
    print(i)

#Sorted Function:
sorted_Students=sorted(students,reverse=True)
for i in sorted_Students:
    print(i)

students_2=[("Piyush",20),
            ("Anant",21),
            ("Aman",19)]
grades=lambda grades:grades[0]
students_2.sort(key=grades)
for i in students_2:
    print(i)

("\n")
#Map:
#The map() function applies a given function to each item of an iterable (such as a list
#or tuple) and returns a map object.
#The map() function takes two arguments: function and iterable.

store=[
    ("Shirt",20),
    ("Pant",30),
    ("Shoes",40),
    ("Watch",50)]
store_dollar=lambda data:(data[0],data[1]*85)
store_map=list(map(store_dollar,store))
for i in store_map:
    print(i)

#Filter:
#The filter() function constructs an iterator from elements of an iterable for which a function returns true.
#It actually filters the iterables on which function is applied
friends=[
    ("Rahul",20),
    ("Piyush",21),
    ("Aman",19),
    ("Priya",16)]
drinking_age=lambda n:n[1]>=18
drinking_buddies=list(filter(drinking_age,friends))
for i in drinking_buddies:
    print(i)

#Reduce Function:
#The reduce() function applies a rolling computation to sequential pairs of values in a list.
from functools import reduce
word=["H","E","L","L","O"]
fun_word=lambda x,y:x+y
word_join=reduce(fun_word,word)
print(word_join)

num=[1,2,3,4,5]
fac_=lambda x,y:x*y
num_product=reduce(fac_,num)
print(num_product)

#List Comprehensions:
#List comprehensions provide a concise way to create lists.
    #Common applications of list comprehensions include:
    #filtering elements from a list
    #transforming elements in a list
    #creating new lists from existing lists or other iterables
    #removing duplicates from a list

squares=[i*i for i in range(1,11)]
print(squares)

students=[88,34,22,43,54,23,65,77,87,33,43]
passed_students=list(filter(lambda x:x>=33,students))
print(passed_students)

area=[1000,1200,1300,1400,900,800,500]
func_area=lambda x:x>=1000
area_in_sq_meters=list(filter(func_area,area))
print(area_in_sq_meters)

passed_students=[i for i in students if i>=33]
print(passed_students)

voting=[18,23,43,54,13,65,34,12,54,46,12,13,14,15,16,18]

voting_people=[i for i in voting if i>=18]
print(voting_people)

#Dictionary Comprehension:
#Dictionary comprehensions provide a concise way to create dictionaries.
    #Common applications of dictionary comprehensions include:
    #filtering key-value pairs from a dictionary
    #transforming key-value pairs in a dictionary
    #creating new dictionaries from existing dictionaries or other iterables
    #removing key-value pairs from a dictionary
"Format = {key: expression for (key,value) in iterable}"
cities_in_F={"New York":38,"London":34,"Delhi":45,"UtraKhand":36}
cities_in_C={key:round((value-32)*(5/9))for (key,value) in cities_in_F.items()}
print(cities_in_C)

weather={"New York":"Snowing","Boston":"Sunny","Los-Angeles":"Sunny"}
sunny_weather={key:value for (key,value) in weather.items() if value=="Sunny"}
print(sunny_weather)

teachers=[("Piyush",25),
          ("Sarthak",23),
          ("Anant",18),
          ("Piyush Shukla",54)]
teachers_filter=lambda x:x[1]>=18
teachers_filter_result=list(filter(teachers_filter,teachers))
print(teachers_filter_result)
