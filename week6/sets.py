

# 1

def remove_duplicates(list1: list):
    seti=set(list1)
    return list(seti)

# 2

def count_unique_elements(list1: list):
    seti=set(list1)
    counter=0
    for item in seti:
        counter+=1
    return counter

# 3

def  common_elements(list1, list2):
    return sorted(list(set(list1)&set(list2)))

# 4

def elements_in_only_one(list1, list2):
    return sorted(list(set(list1) ^ set(list2)))

# 5

def is_subset(list1, list2):
    if set(list1)-set(list2):
        return False
    return True

# 6

def unique_characters(str1):
    if len(str1) == len(set(str1)):
        return True
    return False


# 7

def  first_repeated_element(list1):
    seti=set()
    for item in list1:
        if item in seti:
            return item
        seti.add(item)
    return None

# 8

def distinct_words(str1: str):
    str1=set(str1.lower().split(" "))
    return len(str1)

# 9

def pair_sum_exists(list1, target):
    seti=set()
    for num in list1:
        if target-num in seti:
            return True
        seti.add(num)
    return False

# 10

def symmetric_difference_without_operators(list1, list2):
    list1,list2=set(list1),set(list2)
    nwe_list=[item for item in list1|list2 if item not in list1 or item not in list2]
    nwe_list.sort()
    return nwe_list

