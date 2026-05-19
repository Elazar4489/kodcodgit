
# 1

def  sum_of_a_list(les):
    suni=0
    for num in les:
        suni+=num
    return suni

# 2

def maximum_element(les):
    maxi=les[0]
    for num in les:
        if num > maxi:
            maxi=num
    return maxi

# 3

def count_occurrences(les: list, value):
    return les.count(value)

# 4

def revers_a_list(les):
    new_list=[]
    for i in range(len(les)-1,-1,-1):
        new_list.append(les[i])
    return new_list

# 5

def remove_duplicates(les):
    new_list=[]
    for item in les:
        if item not in new_list:
            new_list.append(item)
    return new_list

# 6

def second_largest(les):
    maxi=max(les)
    second=les[0]
    for i in les:
        if i > second and i != maxi:
            second=i
    if maxi==second:
        second=None
    return second

# 7

def merge_two_sorted_lists(les1,les2):
    new_list=les1+les2
    new_list.sort()
    return new_list

# 8

def rotate_a_list(les: list, k):
    for i in range(k):
        les.insert(0,les.pop(-1))
    return les
