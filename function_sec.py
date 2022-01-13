def get_names(students):
    '''return list of cities from the students list'''
    result = []

    for student in students:
        if student.get("name"):
            result.append(student.get("name"))
        else:
            return ('error')

    return(result)


print(get_names(students))
