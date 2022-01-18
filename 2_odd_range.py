def odd_range(end):
    array = []

    for i in range(end + 1):
        if(i % 2 == 1):
            array.append(i)

    return array


print(odd_range(6))
