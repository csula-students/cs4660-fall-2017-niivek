"""Lists defines simple list related operations"""

mainLi = [1,2,3,4,5,6,7]

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

print(get_first_item(mainLi))

print(get_last_item(mainLi))

print(get_second_and_third_items(mainLi))

print(get_sum(mainLi))

print (get_avg(mainLi))
