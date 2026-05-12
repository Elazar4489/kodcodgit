


def is_even(n):
    if n%2==0:
        return True
    return False


def factorial(n):
    result=1
    for i in range(2,n+1):
        result=result*i
    return result


def is_palindrome(s):
    s1=s[::-1]
    if s==s1:
        return True
    return False


def sum_digits(n):
    while n >= 10:
        n=str(n)
        nn=0
        for i in n:
            nn+=int(i)
        n=int(nn)
    return n


def count_digits(n):
    conter=0
    while n:
        n=n//10
        conter+=1
    return conter


def reverse_integer(n):
    reverse_number=0
    while n:
        reverse_number = reverse_number * 10
        reverse_number+=(n%10)
        n=n//10
    return reverse_number


def move_all_0s(l: list):
    n=len(l)-1
    while n > 0:
        if l[n]==0:
            l.append(l.pop(n))
        else:
            n-=1
    return l


def results(les: list):
    print(sum(les))
    print(sum(les)/len(les))
    print(min(les))
    print(max(les))
    return None

def reverse_list(les: list):
    new_les=[]
    n=len(les)
    while n > 0:
        new_les.append(les.pop())
        n-=1
    return new_les


def repeating_values(les: list):
    new_les=[]
    for item in les:
        if item not in new_les:
            new_les.append(item)
    return new_les






a=repeating_values([2,3,55,6,33,3,3,3,3,3,3,2,44,6,55])
print(a)
