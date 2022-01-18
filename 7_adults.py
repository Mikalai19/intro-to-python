'''
/***********************************************************************
Write a function `adults(people)` that takes in an array of person
objects. The function should return an array containing the names of
those who have an age of 18 or higher.
Example:
ppl = [
  {'name': 'Khalid Robinson', 'age': 22},
  {'name': 'Ariel Winter', 'age': 20},
  {'name': 'Post Malone', 'age': 25},
  {'name': 'Willow Smith', 'age': 17}
]
print(adults(ppl)); # => [ 'Khalid Robinson', 'Post Malone' ]
***********************************************************************/
'''


def adults(people):
    name = []
    peoples = people[i]
    for i in range(len(people)):
        if(peoples["age"] >= 18):
            name.append(peoples["name"])
    return name


ppl = [
    {'name': 'Khalid Robinson', 'age': 22},
    {'name': 'Ariel Winter', 'age': 20},
    {'name': 'Post Malone', 'age': 25},
    {'name': 'Willow Smith', 'age': 17}
]

print(adults(ppl))
