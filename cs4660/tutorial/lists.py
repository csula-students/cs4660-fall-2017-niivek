"""Lists defines simple list related operations"""

def get_first_item(li):
    return li[0]
    pass

def get_last_item(li):
    return li[len(li)-1]
    pass

def get_second_and_third_items(li):
    return li[1:3]
    pass

def get_sum(li):
    return sum(li)
    pass

def get_avg(li):
    return sum(li)/(len(li)-1)
    pass

print(get_first_item([1,2,3,4,5,6,7]))

print(get_last_item([1,2,3,4,5,6,7]))

print(get_second_and_third_items([1,2,3,4,5,6,7]))

print(get_sum([1,2,3,4,5,6,7]))

print (get_avg([1,2,3,4,5,6,7]))
