'''
/***********************************************************************
Write a function `value_pair(obj1, obj2, key)` that takes in two objects
and a key (string). The function should return an array containing the
corresponding values of the objects for the given key.
Examples:
object_1 = {'name': 'One', 'location': 'Remote', 'age': 1}
object_2 = {'name': 'Two', 'location': 'San Francisco'}
print(value_pair(object_1, object_2, 'location')) # => [ 'Remote', 'San Francisco' ]
print(value_pair(object_1, object_2, 'name')) # => [ 'One', 'Two' ]
***********************************************************************/
'''


def value_pair(obj1, obj2, key):
    one = obj1[key]
    two = obj2[key]
    pair = [one, two]
    return pair


object_1 = {
    "name": "One",
    "location": "Remote",
    "age": 1
}

object_2 = {
    "name": "Two",
    "location": "San Francisco"

}

print(value_pair(object_1, object_2, "location"))
print(value_pair(object_1, object_2, "name"))
