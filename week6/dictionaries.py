

# 1

def sum_of_values(dicti: dict):
    sumi=0
    for val in dicti.values():
        sumi+=val
    return sumi

# 2

def key_with_maximum_value(dicti: dict):
    for k, v in dicti.items():
        if v==max(dicti.values()):
            return k
    return None

# 3

def count_characters(stri):
    dicti={}
    for i in stri:
        if i not in dicti:
            dicti[i]=1
        else:
            dicti[i]+=1
    return dicti

# 4

def invert_a_dictionary(dicti):
    new_dict={}
    for k,v in dicti.items():
        new_dict[v]=k
    return new_dict

# 5

def merge_two_dictionaries(dict1: dict, dict2: dict):
    dict1.update(dict2)
    return dict1.copy()

# 6

def filter_by_value(dicti, threshold):
    new_dict={}
    for k, v in dicti.items():
        if v > threshold:
            new_dict[k]=v
    return new_dict

# 7

def group_by_first_letter(les):
    new_dict={}
    for word in les:
        if word[0] not in new_dict:
            new_dict[word[0]]=[word]
        else:
            new_dict[word[0]].append(word)
    return new_dict

# 8

def word_frequency(str1):
    lst = str1.split(" ")
    new_dict={}
    for i in lst:
        new_dict[i]=lst.count(i)
    return new_dict


# 9

def common_keys(dict1, dict2):
    les=[k for k in dict1 if k in dict2]
    return les

# 10

def most_frequent_value(dict1: dict):
    new_dict={}
    for v in dict1.values():
        if v in new_dict:
            new_dict[v]+=1
        else:
            new_dict[v]=1
    l=[k for k, v in new_dict.items() if v==max(new_dict.values())]
    return l


