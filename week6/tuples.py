


# 1

def sum_of_a_tuple(tp):
    sum_of_tuple_elements=0
    for element in tp:
        sum_of_tuple_elements+=element
    return sum_of_tuple_elements

# 2

def maximum_elements(tp):
    maxi=tp[0]
    for element in tp:
        if element > maxi:
            maxi=element
    return maxi

# 3

def count_occurrences1(tp,val):
    counter=0
    for item in tp:
        if item == val:
            counter+=1
    return counter

# 4

def revers_a_tuple(tp):
    new_tp=[]
    for item in range(len(tp)-1,-1,-1):
        new_tp.append(tp[item])
    return tuple(new_tp)

# 5

def swap_pairs(even_tuple):
    new_tuple=[]
    n=len(even_tuple)
    for i in range(0,n,2):
        a,b=even_tuple[i],even_tuple[i+1]
        new_tuple.append(b)
        new_tuple.append(a)
    return tuple(new_tuple)

# or...

def swap_pairs1(even_tuple):
    new_tuple = []
    n = len(even_tuple)
    while n >0:
        new_tuple.append(even_tuple[-n+1])
        new_tuple.append(even_tuple[-n])
        n-=2
    return tuple(new_tuple)

# 6

def min_and_max(tp):
    maxi=tp[0]
    mini=tp[0]
    for num in tp:
        if num > maxi:
            maxi=num
        if num < mini:
            mini=num
    return (mini, maxi)

# 7

def distance_between_points(tp1, tp2):
    x1, y1=tp1[0],tp1[1]
    x2, y2=tp2[0],tp2[1]
    distance=((x2-x1)**2+(y2-y1)**2)**0.5
    return distance

# 8

def merge_and_sort(tp1, tp2):
    new_tuple=[*tp1,*tp2]
    new_tuple.sort()
    return tuple(new_tuple)

# 9

def  frequency_table(tp):
    new_tuple=[]
    for item in tp:
        tuple_for_item=(item,tp.count(item))
        if tuple_for_item not in new_tuple:
            new_tuple.append(tuple_for_item)
    return tuple(new_tuple)

# 10

def rotate_a_tuple(tp, k):
    new_tuple=list(tp)
    for i in range(k):
        new_tuple.insert(0,new_tuple.pop(-1))
    return tuple(new_tuple)


